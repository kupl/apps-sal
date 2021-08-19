N = int(input())
ans = int(N * (N - 1) // 2)
if N == 1:
    print(0)
else:
    print(ans)
