ii = lambda: int(input())
mi = lambda: list(map(int, input().split()))
li = lambda: list(mi())

b, k = mi()
a = li()
b = b % 2
c = 1
ans = 0
for x in a[::-1]:
    ans = (ans + c * x) % 2
    c *= b
print('odd' if ans else 'even')


