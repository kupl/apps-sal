n = int(input())
a = []
b = []
s1 = 0
s2 = 0
k = 0
for i in range(n):
    (x, y) = map(int, input().split())
    a.append(x)
    b.append(y)
    s1 += x
    s2 += y
if s1 % 2 == 0 and s2 % 2 == 0:
    print(0)
elif s1 % 2 == 0 and s2 % 2 != 0 or (s1 % 2 != 0 and s2 % 2 == 0):
    print(-1)
else:
    for i in range(n):
        if a[i] % 2 == 1 and b[i] % 2 == 0 or (a[i] % 2 == 0 and b[i] % 2 == 1):
            print(1)
            break
        k += 1
if k == n:
    print(-1)
