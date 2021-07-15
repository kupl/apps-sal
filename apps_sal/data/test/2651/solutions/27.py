n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

#普通に考えるのであればnC2 * mC2

# 累積和使えばあるx_iを選んだときの横の長さの和(もう１本のx_iとの距離の合計)は分かる
mod = 10**9 + 7
# H = x[-1] - x[0]
# W = y[-1] - y[0]
# S = H*W % mod
# S *= (n-1)*(m-1)
# if n >= 4:
#     h = x[-2] - x[1]
#     S -= h*W * 2
# if m >= 4:
#     w = y[-2] - y[1]
#     S -= H*w * 2
H = 0
W = 0
for i in range(n//2):
    w = x[n-1-i] - x[i]
    if i == n//2 - 1:
        if n % 2 == 1:
            w *= 2
    else:
        w *= n-2*i-1
    W += w
    W %= mod
for j in range(m // 2):
    h = y[m-1-j] - y[j]
    if j == m//2 - 1:
        if m % 2 == 1:
            h *= 2
    else:
        h *= m-1-2*j
    H += h
    H %= mod
S = H*W

print((S % mod))

