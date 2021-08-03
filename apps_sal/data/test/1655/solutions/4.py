def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
L = li()
L.reverse()
t = 0
p = -1
for i in range(n):
    if i > p:
        t += i - p
    p = max(p, i + L[i])
print(t)
