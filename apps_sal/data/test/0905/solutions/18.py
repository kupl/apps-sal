a, b = map(int, input().split(' '))
maxx = 0
mark = False
for i in range(a):
    c, d = map(int, input().split(' '))
    if 100 * c + d <= 100 * b:
        mark = True
        if d > 0:
            maxx = max(100 - d, maxx)
if mark == True:
    print(maxx)

else:
    print(-1)
