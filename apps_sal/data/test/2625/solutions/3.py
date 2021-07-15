def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

for n in range(ii()):
    k, x = mi()
    ans = 9 * (k - 1) + x
    print(ans)

