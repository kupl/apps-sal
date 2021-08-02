N, K = map(int, input().split())
ans = 0
if K % 2 == 1:
    print((N // K)**3)
else:
    ans = (N // K)**3
    k = K // 2
    j = (N + k) // K
    print(j**3 + ans)
