t = int(input())
a = set()
for i in range(1, 10):
    s = str(i)
    for j in range(1, 11):
        a.add(int(j * s))
b = list(a)
b.sort()
for i in range(t):
    n = int(input())
    j = 0
    while b[j] <= n:
        j += 1
    print(j)
