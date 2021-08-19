(n, x) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
f = [False] * (max(a) + 1)
for i in a:
    if f[i]:
        print(0)
        quit()
    f[i] = True
wk1 = []
for i in range(n):
    wk1.append(a[i] & x)
f = [False] * (max(a) + 1)
position = [-1] * (max(a) + 1)
for i in range(n):
    f[a[i]] = True
    position[a[i]] = i
for i in range(n):
    if f[wk1[i]] and position[wk1[i]] != i:
        print(1)
        quit()
f = [False] * (max(wk1) + 1)
for i in wk1:
    if f[i]:
        print(2)
        quit()
    f[i] = True
print(-1)
