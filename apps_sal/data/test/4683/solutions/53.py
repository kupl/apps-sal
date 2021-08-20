N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
sum_list = []
sum_ = 0
for i in range(len(A) - 1):
    sum_ += A[i + 1]
    sum_list.append(sum_)
len_ = 0
for i in range(len(A) - 1):
    len_ += A[i + 1] * (sum_list[-1] - sum_list[i]) % mod
print((len_ + A[0] * sum_list[-1]) % mod)
