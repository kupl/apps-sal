from sys import stdin as cin
from sys import stdout as cout


def main():
    n = int(cin.readline())
    a = list(map(int, cin.readline().split()))
    kol1 = 0
    kol2 = 0
    for i in a:
        if i == 1:
            kol1 += 1
        else:
            kol2 += 1
    o = 0
    if kol2 <= kol1:
        o = kol2
        kol1 -= kol2
        kol2 = 0
    else:
        o = kol1
        kol2 -= kol1
        kol1 = 0
    cout.write(str(o + kol1 // 3))


main()
