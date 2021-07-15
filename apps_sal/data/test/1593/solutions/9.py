n, k = map(int, input().split())
if k >= 1000000:
    print('0')
    return
def f():
    x, y, d = map(int, input().split())
    return (x * x + y * y, d)
t = [f() for i in range(n)]
t.sort()
for r, d in t:
    k += d
    if k >= 1000000:
        print(r ** 0.5)
        break
else: print('-1')
