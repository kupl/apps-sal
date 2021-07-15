import sys
readline = sys.stdin.readline

def ceil(a, b):
    return -(-a//b)

def main():
    N = int(readline())
    inp = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]
    scr_t, scr_a = 1, 1
    for t, a in inp:
        n = max(ceil(scr_t, t), ceil(scr_a, a))
        scr_t = n * t
        scr_a = n * a

    print(scr_t + scr_a)

def __starting_point():
    main()
__starting_point()
