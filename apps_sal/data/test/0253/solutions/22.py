def R():
    return map(int, input().split())


a = list(R())
ans = 0
o = a.count(1)
t = a.count(2)
th = a.count(3)
f = a.count(4)
if o > 0 or t > 1 or th > 2 or (t == 1 and f == 2):
    print('YES')
else:
    print('NO')
