N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

# result = 0
# for i in range(N):
#     for j in range(N):
#         if i < j:
#             result += (A[i] * A[j]) % mod

# print(result % mod)

# result = 0
# for i in range(N):
#     j = i+1

#     while(j < N):
#         result += (A[i] * A[j]) % mod
#         #print(i, " : ", j)
#         j += 1

# print(result % mod)

A_sum = sum(A)
result = 0
for i in range(N):
    A_sum = A_sum - A[i]
    result += (A[i] * A_sum) % mod

print(result % mod)
