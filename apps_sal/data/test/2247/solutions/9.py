def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

for t in range(ii()):
    s, a, b, c = mi()
    n = s // c
    x = n // a
    ans = n + x * b
    print(ans)

