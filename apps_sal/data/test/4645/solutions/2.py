#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|  
#  code

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 2 or n == 3:
            print(-1)
            continue
        if n == 4:
            print('3 1 4 2')
            continue
        a = [2 * i + 1 for i in range((n + 1) // 2)]
        a.append(a[-1] - 3)
        if a[-1] + 2 == (n // 2) * 2:
            a.append(a[-1] + 2)
        else:
            a.append(a[-1] + 4)
        b = [2 * i + 2 for i in range(n // 2)]
        b = b[::-1]
        for i in b:
            if i not in a:
                a.append(i)
        print(*a)
    return

def __starting_point():
    main()
__starting_point()
