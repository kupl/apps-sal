from sys import stdin as cin
from sys import stdout as cout

def main():
    n, h, a, b, k = list(map(int, cin.readline().split()))
    for i in range(k):
        ta, fa, tb, fb = list(map(int, cin.readline().split()))
        if ta == tb:
            print(abs(fa - fb))
        else:
            o = abs(ta - tb)
            if fa < a and fb < a:
                o += 2 * a - fa - fb
            elif fa > b and fb > b:
                o += fa + fb - 2 * b
            else:
                o += abs(fb - fa)
            print(o)

main()

