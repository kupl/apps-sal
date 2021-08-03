u, v = map(int, input().split())
if u > v or (v - u) % 2 == 1:
    print(-1)
    return
v = (v - u) // 2
a = u | v
b = v
c = u & v
if a == 0:
    print(0)
elif b == 0:
    print(1)
    print(a)
elif c == 0:
    print(2)
    print(a, b)
else:
    print(3)
    print(a, b, c)
