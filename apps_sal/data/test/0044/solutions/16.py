(D, K, A, B, T) = list(map(int, input().split()))


def nStops(N):
    if N == 0:
        return 0
    else:
        return (N - 1) // K


case1 = D * B
case2 = A * D + T * nStops(D)
ans = min(case1, case2)
for i in range(max(0, D - 1000000), D + 1):
    ans = min(ans, A * i + B * (D - i) + T * nStops(i))
print(ans)
