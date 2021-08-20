import collections
n = int(input())
mod = 10 ** 9 + 7


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


tmp = collections.defaultdict(int)
for i in range(1, n + 1):
    for (j, k) in factorization(i):
        tmp[j] += k
ans = 1
for (tei, si) in list(tmp.items()):
    if tei == 1:
        continue
    else:
        ans *= si + 1
        ans %= mod
print(ans)
