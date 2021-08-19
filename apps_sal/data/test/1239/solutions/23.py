n = int(input())
L = input()
l = L.split()
l = [int(x) for x in l]
l.sort()
m = l[1] - l[0]
for i in range(n - 1):
    if l[i + 1] - l[i] < m:
        m = l[i + 1] - l[i]
p = 0
for i in range(n - 1):
    if l[i + 1] - l[i] == m:
        p += 1
print(m, p, sep=' ')
