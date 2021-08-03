n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
d = []
ans = 0

for i in a:
    if len(d) > 0 and d[0] < i - m + 1:
        del d[0]

    if len(d) < k - 1:
        d.append(i)
    else:
        ans += 1

print(ans)
