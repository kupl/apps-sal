(n, b, t) = (int(i) for i in input().split())
c = [0] * b
a = []
for i in range(n):
    s = input()
    a.append(s)
    for j in range(len(s)):
        c[j] += a[i][j] == 'Y'
a = 0
for i in range(b):
    a += c[i] >= t
print(a)
