import copy

def main():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    PX = []
    for i in range(M):
        P, X = list(map(int, input().split()))
        tmp = copy.copy(T)
        tmp[P-1] = X
        print((sum(tmp)))

def __starting_point():
    main()

__starting_point()
