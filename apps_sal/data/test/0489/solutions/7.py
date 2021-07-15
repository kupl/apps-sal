## 2

def c(x, y):
    a = b = 1
    for i in range(y):
        a *= x-i
        b *= y-i
    return int(a/b)

n = int(input())
a = list(map(int, input().split()))
if n < 3:
    print(0)
a.sort()
x1, x2, x3 = a[0], a[1], a[2]
count = 0
for i in range(n):
    if a[i] == x3:
        count += 1
if x1==x2 and x2==x3:
    print(c(count, 3))
elif x1<x2 and x2==x3:
    print(c(count, 2))
else:
    print(count)
    

