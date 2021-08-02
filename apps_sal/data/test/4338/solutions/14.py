import random


def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n, x, y = tuple(mi())
a = li()
random.shuffle(a)
a = sorted(a)
c1 = 0
c2 = 0
for i in a:
    if i <= x:
        c1 += 1
    if i <= y:
        c2 += 1
ans = 0
if x <= y:
    ans = (c1 + 1) // 2
else:
    ans = n
print(ans)
