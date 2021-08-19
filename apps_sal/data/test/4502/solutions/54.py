n = int(input())
a = list(map(int, input().split()))
q = a[::2]
p = a[1::2]
if n % 2 == 0:
    print(*p[::-1], *q)
else:
    print(*q[::-1], *p)
