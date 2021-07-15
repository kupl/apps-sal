from collections import Counter
n, m = list(map(int, input().split()))
x = [[] for i in range(m)]
for i in range(n):
    a = list(map(int, input().split()))
    k = a[0]
    for j in a[1:]:
        x[j - 1].append(i)


ans = 1
MOD = 10 ** 9 + 7
for e in list(Counter(list(map(str, x))).values()):
    for i in range(2, e + 1):
        ans = ans * i % MOD

print(ans)

