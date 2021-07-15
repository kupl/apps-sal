def main():
    import sys
    input = sys.stdin.buffer.readline

    N = int(input())
    win = 0
    for _ in range(N):
        a, k = list(map(int, input().split()))
        while True:
            if a < k:
                g = 0
                break
            elif a % k == 0:
                g = a // k
                break
            else:
                d = (a//k) + 1
                a -= d * ((a - k * (a//k))//d)
                if a < k:
                    g = 0
                    break
                elif a % k == 0:
                    g = a // k
                    break
                else:
                    a -= d

        win ^= g
    if win:
        print('Takahashi')
    else:
        print('Aoki')


def __starting_point():
    main()

__starting_point()
