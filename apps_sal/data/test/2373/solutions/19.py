n = int(input())
p = [0] + list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    if p[i] == i:
        if i != n:
            tmp = p[i]
            p[i] = p[i + 1]
            p[i + 1] = tmp
            ans += 1
        else:
            tmp = p[i]
            p[i] = p[i - 1]
            p[i - 1] = tmp
            ans += 1
# print(p[1:])
print(ans)
