#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|  
#  code

def main():
    t = int(input())
    for _ in range(t):
        x,y,a,b = map(int,input().split())
        i = (y - x)//(a + b)
        if x + a * i == y - b * i:
            print(i)
        else:
            print(-1)
    return

def __starting_point():
    main()
__starting_point()
