import sys
inp = sys.stdin
n, t = inp.readline().split()
n, t = int(n), int(t)
s = inp.readline()
a = []
for i in range(n):
    a.append(s[i])
for i in range(t):
    j = 0
    while j < n - 1:
        if a[j] == 'B' and a[j + 1] == 'G':
            a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        j += 1
print("".join(a))
