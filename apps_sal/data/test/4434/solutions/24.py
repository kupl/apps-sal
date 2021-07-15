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
        ans = 0
        for i in range(1,n + 1,2):
            ans += (4 * i - 4) * (i // 2)
        print(ans)
    return

def __starting_point():
    main()
__starting_point()
