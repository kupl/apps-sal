(n, l) = map(int, input().split())
a = []
for i in range(l, n + l):
    a.append(i)
if a[0] > 0:
    b = a.pop(0)
elif a[n - 1] < 0:
    b = a.pop(n - 1)
else:
    for j in range(n):
        if a[j] == 0:
            b = a.pop(j)
            break
print(sum(a))
