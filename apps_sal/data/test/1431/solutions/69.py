n = int(input())
a = [int(x) for x in input().split()]
m = []
for i in range(n, 0, -1):
    t = 0
    for j in range(i, n + 1, i):
        t = t + a[j - 1]
    if t % 2 != a[i - 1]:
        if a[i - 1] == 1:
            a[i - 1] = 0
        else:
            a[i - 1] = 1
    if a[i - 1] == 1:
        m.append(i)
print(len(m))
for i in m:
    print(i)
    print(" ")
