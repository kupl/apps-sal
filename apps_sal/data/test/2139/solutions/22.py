s = input()
a = list(map(len, s.split('bear')))
n = len(a)
for i in range(n):
    if 0 < i < n - 1:
        a[i] += 4
    else:
        a[i] += 1
k = r = 0
for i in range(n - 1):
    k += a[i]
    r += a[i] * (len(s) - k - 2)
print(r)
