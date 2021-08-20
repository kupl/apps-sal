import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (X, Y, Z, K) = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    C = list(map(int, readline().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = [a + b for a in A[:K] for b in B[:K]]
    AB.sort(reverse=True)
    ABC = [ab + c for ab in AB[:K] for c in C[:K]]
    ABC.sort(reverse=True)
    print(*ABC[:K], sep='\n')
    return


def __starting_point():
    main()


__starting_point()
