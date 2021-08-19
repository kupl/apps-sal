N = int(input())
p = list(map(int, input().split()))

# 条件はN=O(10^5)よりO(N)で解く
# 二重ループをすると、O(N^2)で間に合わない
# 累積和の問題（ABC-154-Dとか）と同じ発想が使える！

# 具体的にO(N)で解くために、最初に各iに対して、i番目までの最小値を求めておく
m = [0] * (N)
m[0] = p[0]
for i in range(1, N):
    m[i] = min(m[i - 1], p[i])

# 各iまでの最小値とi番目の値を比較し、最小値の方が大きければよい
ans = 1
for i in range(1, N):
    if m[i - 1] >= p[i]:
        ans += 1

print(ans)
