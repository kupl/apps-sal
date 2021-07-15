CA = ['C', 'M', 'Y']


def solve():
    n, m = list(map(int, input().split()))
    c = [input().split() for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if c[i][j] in CA:
                print('#Color')
                return
    print('#Black&White')


def main():
    solve()


def __starting_point():
    main()

__starting_point()
