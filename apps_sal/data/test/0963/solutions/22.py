def main():
    n, k = list(map(int, input().split()))
    lr = [list(map(int, input().split())) for _ in [0]*k]
    bit = [0]*(n+1)
    bit[1] = 1
    mod = 998244353
    for i in range(1, n+1):
        if i+1 < n:
            bit[i+1] = (bit[i+1]+bit[i]) % mod
        k = bit[i]
        for l, r in lr:
            l += i
            if l > n:
                continue
            bit[l] = (bit[l]+k) % mod
            r += i+1
            if r <= n:
                bit[r] = (bit[r]-k) % mod
    print((bit[n] % mod))


main()

