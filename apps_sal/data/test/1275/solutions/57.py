(N, K) = list(map(int, input().split()))
K = abs(K)
ans = 0
for i in range(K + 2, 2 * N + 1):
    Big = i
    Small = i - K
    if Big <= N + 1:
        pattern_of_big = Big - 1
    else:
        tmp = Big - N
        pattern_of_big = N - tmp + 1
    if Small <= N + 1:
        patter_of_small = Small - 1
    else:
        tmp = Small - N
        patter_of_small = N - tmp + 1
    ans += pattern_of_big * patter_of_small
print(ans)
