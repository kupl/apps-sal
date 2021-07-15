import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    X,Y = list(map(int,input().split()))
    if abs(X - Y) <= 1:
        print('Brown')
    else:
        print('Alice')
def __starting_point():
    main()

__starting_point()
