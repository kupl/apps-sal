def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

for i in range(ii()):
    x = ii()
    ok = 0
    while x >= 0:
        if x % 3 == 0:
            ok = 1
            break
        x -= 7
    print('YES' if ok else 'NO')
    

