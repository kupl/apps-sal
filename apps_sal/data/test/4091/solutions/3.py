(n, k) = map(int, input().split())
a = sorted(enumerate(map(int, input().split())), key=lambda x: -x[1])[:k]
s = 0
for i in a:
    s += i[1]
a.sort(key=lambda x: x[0])
print(s)
prev = -1
for i in a[:-1]:
    print(i[0] - prev, end=' ')
    prev = i[0]
print(n - prev - 1)
