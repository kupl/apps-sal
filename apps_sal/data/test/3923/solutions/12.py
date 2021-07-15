#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|  
#  code

def main():
    n , a , b = map(int , input().split())
    if a < b:
        a , b = b , a
    s = []
    k = 1
    ok = False
    x = 0
    y = 0
    for j in range(n):
        kk = n - a * j
        if kk >= 0:
            if kk % b == 0:
                ok = True
                x = j
                y = kk // b
                break
    if not ok:
        print(-1)
        return
    for j in range(x):
        for i in range(a - 1):
            s.append(k + i + 1)
        s.append(k)
        k += a
        n -= a
    for j in range(y):
        for i in range(b - 1):
            s.append(k + i + 1)
        s.append(k)
        k += b
        n -= b
    print(*s)
    return

def __starting_point():
    main()
__starting_point()
