
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
x = a[:n // 2]
a = a[n // 2:]
l, k, m = [], 0, 0
for i in range(n):
    if i % 2 == 0:
        l.append(a[k])
        k += 1
    else:
        l.append(x[m])
        m += 1
m = 0
for i in range(1, n - 1):
    if(l[i] < l[i - 1] and l[i] < l[i + 1]):
        m += 1
print(m)
for i in l:
    print(i, end=" ")
