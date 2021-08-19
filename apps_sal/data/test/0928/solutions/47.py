import bisect
N, K = map(int, input().split())
A = list(map(int, input().split()))
sum_A = [0]
for i in range(N):
    sum_A.append(sum_A[i] + A[i])
# print(sum_A)
re_sum_A = [0]
for i in range(N):
    re_sum_A.append(re_sum_A[i] + A[N - 1 - i])
count = 0
maximum = sum_A[N]
for i in range(N):
    num = maximum - K - sum_A[i]
    index = bisect.bisect(re_sum_A, num)
    count = index + count
print(count)
