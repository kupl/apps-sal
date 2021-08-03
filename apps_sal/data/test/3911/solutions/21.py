n = int(input())
a = []
for i in range(n):
    a.append(1)
    while len(a) > 1 and a[len(a) - 1] == a[len(a) - 2]:
        a.pop()
        a[len(a) - 1] += 1
for i in a:
    print(i, end=' ')
