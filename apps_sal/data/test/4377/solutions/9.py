#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|  
#  code

from collections import Counter
def __starting_point():
    d = list(map(int,input().split()))
    d.sort()
    a = d[0]
    b = d[1]
    c = d[2]
    d = d[3]
    x = d - a
    y = d - b
    z = d - c

    print(x,y,z)
__starting_point()
