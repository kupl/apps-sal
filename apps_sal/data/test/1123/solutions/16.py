def modpow(val, n, mod):
    ret = 1
    while n:
        if n & 1:
            ret = (ret * val) % mod
        val = (val * val) % mod
        n = n >> 1
    return ret


mod = 10 ** 9 + 7
n, k = list(map(int, input().split()))

my_dict = dict()
ret = 0

for i in range(k, 0, -1):
    tmp = modpow(k // i, n, mod)
    cnt = 2
    while True:
        val = i * cnt
        if val > k:
            break
        else:
            cnt += 1
            tmp -= my_dict[val]
    my_dict[i] = tmp
    ret += tmp * i % mod

print((ret % mod))

