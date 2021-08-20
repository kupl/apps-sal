(N, M) = list(map(int, input().split()))
As = list(map(int, input().split()))
ans = 0
(numSts, numEns, sumEns) = ([0] * (2 * M), [0] * (2 * M), [0] * (2 * M))
for i in range(N - 1):
    (A, B) = (As[i] - 1, As[i + 1] - 1)
    if A > B:
        B += M
    ans += B - A
    if B - A > 1:
        numSts[A + 2] += 1
        numEns[B + 1] += 1
        sumEns[B + 1] += B - A - 1
nums = [0] * M
num = 0
k = 0
for i in range(2 * M):
    k += numSts[i] - numEns[i]
    num += k
    num -= sumEns[i]
    nums[i % M] += num
print(ans - max(nums))
