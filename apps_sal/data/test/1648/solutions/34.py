N, K = list(map(int, input().split()))

# x_1 + x_2 + ... x_k = n
# x_i >= 0
# k個の箱にn個のボールを入れる重複組み合わせ　n+k-1_C_k-1
# n個の玉とk-1個の仕切りを並べる

# x_1 + x_2 + ... x_k = n
# x_i >= 1
# k個の箱にn個のボールを1個以上入れる重複組み合わせ　n-1_C_k-1
# n個の玉の仕切りn-1個の中に、k-1箇所仕切りを入れる

from math import factorial

# k = 1,2,...,K
for k in range(1, K + 1):
    if k > N - K + 1:
        print((0))
        continue

    # k = 1,2,...,K
    # K個の青いボールをk個に分割する方法
    # K-1_C_k-1
    c1 = factorial(K - 1) // (factorial(K - k) * factorial(k - 1))
    c1 = int(c1) % (10 ** 9 + 7)

    # N-K個の赤いボールの分割
    # k+1個に分割(しかし両端はなくても良い)
    # N-K+1_C_k

    # x_1 + x_2 + ... + x_k + x_k+1 = N−K
    # x1 >= 0
    # x_2,x_3,...,x_k >= 1
    # x_k + 1 >= 0

    c2 = factorial(N - K + 1) // (factorial(N - K - k + 1) * factorial(k))
    c2 = int(c2) % (10**9 + 7)

    ans = c1 * c2 % (10**9 + 7)
    print(ans)

