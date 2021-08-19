(k, n) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = a + [n * k + 1]
b.sort()
j = 1
t = []
for i in b:
    t += list(range(j, i))
    j = i + 1
x = 0
k -= 1
for i in range(n):
    print(str(a[i]) + ' ' + ' '.join((str(j) for j in t[x:x + k])))
    x += k
