from itertools import product
n = int(input())
a = list(map(int, input().split()))
k = 1
cnt = []
for i in product([0, 1], repeat=n):
    k = 1
    v = 0
    for j in range(n):
        k = k * 2 + i[j]
        if k - 2 < len(a):
            v += a[k - 2]
    cnt.append(v)
mini = -1
for i in range(len(cnt)):
    if cnt[i] > mini:
        mini = cnt[i]

ans = 0
for i in range(1, n + 1):
    minicur = -1
    k = 0
    k1 = 2**(n - i)
    for j in range(2**i):
        minicur = -1
        for l in range(k, k1):
            if cnt[l] > minicur:
                minicur = cnt[l]
        for l in range(k, k1):
            cnt[l] += (mini - minicur)
        ans += mini - minicur
        k += 2**(n - i)
        k1 += 2**(n - i)


print(ans)
