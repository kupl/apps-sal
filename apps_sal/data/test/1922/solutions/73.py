N, M = list(map(int, input().split()))
if N == 1 and M == 1:
    ans = 1
elif N == 1:
    ans = M - 2
elif M == 1:
    ans = N - 2
elif N == 2 or M == 2:
    ans = 0
else:
    ans = (N * M) - (2 * N + 2 * M - 4)

print(ans)

