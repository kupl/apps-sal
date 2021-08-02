def maxSubarrayXOR(lis, n, INT_BITS=60):
    idx = 0
    for i in range(INT_BITS - 1, -1, -1):
        Mele = -1
        bit_i = 1 << i
        for j in range(idx, n):
            if lis[j] & bit_i and lis[j] > Mele:
                Midx, Mele = j, lis[j]
        if Mele < 0: continue
        lis[Midx], lis[idx] = lis[idx], lis[Midx]
        for j in range(n):
            if j != idx and lis[j] & bit_i:
                lis[j] ^= lis[idx]
        idx += 1
    res = 0
    for x in lis: res ^= x
    return res


n = int(input())
a = list(map(int, input().split()))
t = 0
for x in a: t ^= x
b = [x ^ (x & t) for x in a]
print(t + maxSubarrayXOR(b, n) * 2)
