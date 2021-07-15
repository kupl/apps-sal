n = int(input())

a = []
for i in range(n):
    a.append(input())
if n<2:
    print(1)
    return
a.sort()
b = []
k = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        k += 1
    else:
        b.append(k+1)
        k = 0
    if i == n-2:
        b.append(k+1)
b.sort()
print(b[len(b)-1])


