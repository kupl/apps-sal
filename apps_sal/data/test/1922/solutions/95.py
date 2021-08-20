(N, M) = list(map(int, input().split()))
if N == 2 or M == 2:
    ans = 0
elif N == 1:
    ans = M - 2
elif M == 1:
    ans = N - 2
else:
    ans = (N - 2) * (M - 2)
if ans < 0:
    ans = 1
print(ans)
