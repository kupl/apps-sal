N = int(input())
A = list(map(int, input().split()))

# 各山に降った雨の量
x = [-1] * N

# まずx[0]を求める
# x[0] = s - 2 * (A_2+A_4+...+A_N-1)
s = sum(A)
temp = 0
for i in range(2, N, 2):
    temp += A[i - 1]
x[0] = s - 2 * temp

# x[1],x[2],...,x[N-1]を漸化式から求める
for i in range(1, N):
    x[i] = 2 * A[i - 1] - x[i - 1]
print((*x))
