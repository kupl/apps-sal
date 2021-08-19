n = int(input())
a = list(map(int, input().split()))
a.sort()
n = n / 3
ok = 1
if a.count(1) != n:
    ok = 0
if a.count(5) + a.count(7) > 0:
    ok = 0
p = a.count(2) - a.count(4)
if p < 0:
    ok = 0
if p + a.count(3) != a.count(6):
    ok = 0
if ok == 0:
    print(-1)
else:
    t4 = a.count(4)
    t26 = p
    t36 = a.count(6) - t26
    for i in range(0, t4):
        print(1, 2, 4)
    for i in range(0, t26):
        print(1, 2, 6)
    for i in range(0, t36):
        print(1, 3, 6)
