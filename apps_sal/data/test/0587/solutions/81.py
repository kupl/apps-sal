n, k = list(map(int, input().split()))
td = [list(map(int, input().split())) for _ in range(n)]

td.sort(key=lambda x: x[1], reverse=True)
cand = []
memo = [0 for i in range(n + 1)]

ans = 0
duplicate = []
unique = []
num = 0
i = 0

for t, d in td:
    i += 1
    if i <= k:
        ans += d
        if memo[t]:
            duplicate.append(d)
        else:
            memo[t] = 1
            num += 1
    else:
        if not memo[t]:
            unique.append(d)
            memo[t] = 1

tmp = ans
ans += num * num

# print(tmp, ans)

for d, u in zip(reversed(duplicate), unique):
    tmp += u - d
    num += 1
    ans = max(ans, tmp + num * num)

print(ans)
