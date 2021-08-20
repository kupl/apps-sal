def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


(b, k) = mi()
a = li()
b = b % 2
c = 1
ans = 0
for x in a[::-1]:
    ans = (ans + c * x) % 2
    c *= b
print('odd' if ans else 'even')
