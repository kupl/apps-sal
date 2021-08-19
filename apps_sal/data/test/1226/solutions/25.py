n, a, b = list(map(int, input().split()))
# 2^n-nCa-nCbを求める
# 冪乗を求める関数を求める
# 2のn乗をmで割ったあまりを求める


def pow(a, n, m):
    if n == 0:
        return 1
    else:
        k = pow(a * a % m, n // 2, m)
        if n % 2 == 1:
            k = k * a % m
        return k


# 次は組み合わせを計算する
# まずは前処理をする
inv = [0 for i in range(200001)]
finv = [0 for i in range(200001)]
inv[1] = 1
finv[1] = 1
for i in range(2, 200001):
    # 逆元の求め方p=(p//a)*a+p%a a^(-1)=-(p//a)*(p%a)^(-1)
    inv[i] = (-(1000000007 // i) * inv[1000000007 % i]) % 1000000007
    finv[i] = finv[i - 1] * inv[i] % 1000000007

# nが10^7程度であればnCk=n!*(k!)*((n-k)!)を求めればいい
# nがそれより大きい時は間に合わない。ここでkが小さいことに着目すると
# nCk=n*(n-1).....*(n-k+1)*(k!)^(-1)で求められることがわかる
a_num = 1
b_num = 1
for i in range(n - a + 1, n + 1):
    a_num = i * a_num % 1000000007
for i in range(n - b + 1, n + 1):
    b_num = i * b_num % 1000000007
print(((pow(2, n, 1000000007) - 1 - a_num * finv[a] - b_num * finv[b]) % 1000000007))
