(n, m) = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0
(L, R) = (0, n - 1)
while L < n and ls[L] <= m:
    L += 1
    cnt += 1
while R > L and ls[R] <= m:
    R -= 1
    cnt += 1
print(cnt)
