def main():
    n, k = list(map(int, input().split()))
    MOD = 10**9 + 7

    # 0人部屋が0~k個の時の場合の数の和
    # Σ(i=[0,k]){comb(n,i)*pow((n-i),i)} を求めれば良い
    # しかし上式ではpowの計算量がデカすぎるので、捉え方を変えて下式まで変形
    # Σ(i=[0,k]){comb(n,i)*comb((n-1),i)} を求めれば良い
    # 注:i=0のとき、つまり0人部屋がない、つまり全部屋に1人ずつ、のケースは1通り
    # comb(n,i+1) = comb(n,i) * (n-i)/(i+1) であることを利用する
    ans = 0
    k1 = 1
    k2 = 1
    for i in range(min(k + 1, n)):
        ans += k1 * k2
        ans %= MOD
        k1 *= (n - i) * pow(i + 1, MOD - 2, MOD)
        k1 %= MOD
        k2 *= (n - 1 - i) * pow(i + 1, MOD - 2, MOD)
        k2 %= MOD
    print((int(ans)))


main()
