def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

b = [((1 << (k+1)) - 1) << k for k in range(10)]
b.reverse()
n = ii()
for x in b:
    if n % x == 0:
        print(x)
        break
