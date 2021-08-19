(N, K) = list(map(int, input().split()))
modZeroCount = N // K
modHalfCount = 0
if K % 2 == 0:
    modHalf = K // 2
    if N % K < modHalf:
        modHalfCount = modZeroCount
    else:
        modHalfCount = modZeroCount + 1
answer = modZeroCount ** 3 + modHalfCount ** 3
print(answer)
