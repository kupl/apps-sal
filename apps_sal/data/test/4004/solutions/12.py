n = int(input())
l = [*map(int, input().split())]


def check(x):
    return [abs(e - x) for e in l if e != x]


res = float('inf')
for x in range(1, 101):
    c = check(x)
    if len(set(c)) == 1:
        res = min(res, c[0])
    elif not c:
        res = 0
        break
if res > 100:
    print(-1)
else:
    print(res)
