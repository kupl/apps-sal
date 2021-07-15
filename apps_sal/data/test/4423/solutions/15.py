n = int(input())
r = []
for i in range(n):
    a = list(input().split())
    a[1] = int(a[1])
    a.append(i + 1)
    r.append(a)
r.sort(key = lambda x: x[1], reverse = True)
r.sort(key = lambda x: x[0])
for i in r:
    print(i[2])
