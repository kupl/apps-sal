s = input().strip()
k = int(input())
n = len(s)
a = [False for i in range(n)]
f = list(map(int, input().split()))
for i in range(k):
    f[i] -= 1
    a[f[i]] = not a[f[i]]
rev = False
b = [None for i in range(n)]
for i in range(n // 2 + 1):
    if a[i]:
        rev = not rev
    if rev:
        b[i] = s[-i - 1]
        b[-i - 1] = s[i]
    else:
        b[i] = s[i]
        b[-i - 1] = s[-i - 1]
print(*b, sep='')
