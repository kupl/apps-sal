(N, M) = map(int, input().split())
if N == 1:
    if M == 1:
        ans = 1
    else:
        ans = M - 2
elif M == 1:
    ans = N - 2
else:
    ans = M * N - (2 * N + 2 * M - 4)
print(ans)
