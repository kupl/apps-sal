n = int(input())
l = list(map(int, input().split()))
l.sort()
m = 3 * 1000000000.0
nb = 0
for i in range(len(l) - 1):
    if l[i + 1] - l[i] == m:
        nb += 1
    if l[i + 1] - l[i] < m:
        m = l[i + 1] - l[i]
        nb = 1
print(m, nb, sep=' ', end='\n')
