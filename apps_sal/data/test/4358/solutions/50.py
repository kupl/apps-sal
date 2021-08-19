n = int(input())
L = sorted(list((int(input()) for _ in range(n))))
ans = 0
for i in range(n):
    if i == n - 1:
        ans += L[i] // 2
    else:
        ans += L[i]
print(ans)
