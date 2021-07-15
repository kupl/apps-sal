def main():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        N, M = list(map(int, input().split()))

        S = ((N+1) * N)//2
        zero = N - M
        num = zero // (M+1)
        major = zero % (M+1)
        minor = M+1 - major
        S -= major * (((num+2)*(num+1)) // 2)
        S -= minor * (((num+1)*num) // 2)
        print(S)


def __starting_point():
    main()

__starting_point()
