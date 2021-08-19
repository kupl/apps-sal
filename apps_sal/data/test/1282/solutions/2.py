a = input()
n = len(a)
(o, k) = (0, 0)
for i in range(n):
    if a[i] == 'F':
        k = k + 1
        if i + 1 != k:
            o = max(o + 1, i + 1 - k)
print(o)
