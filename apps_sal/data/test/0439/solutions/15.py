def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n = ii()
m = ii()
n = min(n, 32)
print(m % (2**n))
