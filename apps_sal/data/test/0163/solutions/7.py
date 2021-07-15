n,k = list(map(int,input().split()))
a = input()
g = 0
t = 0

for j in range(n):
    if a[j] == 'G':
        g = j
    if a[j] == 'T':
        t = j
if g < t:
    g, t = t, g
if (g - t) % k == 0:
    per = 0
    for j in range(t, g+1, k):
        if a[j] == '#':
            per = 1
            break
    if per == 1:
        print('NO')
    else:
        print('YES')
else:
    print('NO')

