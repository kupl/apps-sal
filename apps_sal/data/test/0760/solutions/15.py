def tandem(n, a, i):
    for k in range(i, i + n):
        if a[k] != a[k + n] and a[k + n] != '??':
            return 0
    return 1
 
s = list(input().strip())
k = int(input())
s += ['??' for i in range(k)]

res = 0

for i in range(len(s)):
    for n in range(1, (len(s) - i) // 2 + 1):
        if tandem(n, s, i):
            res = max(res, n * 2)
print(res)
