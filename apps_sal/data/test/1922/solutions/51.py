N, M = map(int, input().split())
if N == 1 or M == 1:
    if N == 1 and M == 1:
        print(1)
    else:
        print(max(N, M) - 2)
else:
    ans = (N - 2) * (M - 2)
    print(ans)
