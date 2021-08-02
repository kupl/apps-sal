N, K = list(map(int, input().split()))
ans = 0

if K % 2 == 0:
    d1 = N // (K // 2)
    d2 = N // K
    ans = d2**3 + (d1 - d2)**3
else:
    d = N // K
    ans = d**3

print(ans)
