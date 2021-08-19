from itertools import accumulate
(N, K) = map(int, input().split())
N_s = int(N ** 0.5)
list_a = [1] * N_s
list_b = [N // j - N_s for j in range(1, N_s + 1)]
list_p = [N // j - N_s for j in range(1, N_s + 1)]
for p in range(1, len(list_p)):
    list_p[p - 1] = list_p[p - 1] - list_p[p]
for p in range(1, len(list_b)):
    list_b[p - 1] = list_b[p - 1] - list_b[p]
list_bb = list(reversed(list(accumulate(reversed(list_b)))))
list_aa = list(accumulate(list_a))
mod = 10 ** 9 + 7
for i in range(K - 1):
    temp = sum(list_a)
    list_an = [(temp + list_bb[j]) % mod for j in range(N_s)]
    list_bn = [list_p[j - 1] * list_aa[j - 1] % mod for j in range(1, N_s + 1)]
    list_bbn = list(reversed(list(accumulate(reversed(list_bn)))))
    list_aa = list(accumulate(list_an))
    list_a = list_an
    list_b = list_bn
    list_bb = list_bbn
print((sum(list_a) + sum(list_b)) % mod)
