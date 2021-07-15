#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|  
#  code

def __starting_point():
    n = int(input())
    a =list(map(int,input().split()))
    eve = False
    odd = False
    for i in a:
        if i%2 == 0:
            eve = True
        else:
            odd = True
    if odd and eve:
        print(' '.join(map(str,sorted(a))))
    else:
        print(' '.join(map(str,a)))

__starting_point()
