def main():
    import sys
    input = sys.stdin.readline

    def solve():
        n = int(input())
        s = input()
        l, r = -1, -1
        for i in range(n):
            if s[i] == '1':
                if l == -1:
                    l = i
                r = i

        if l == -1:
            print(n)
        else:
            print(2 * max(r + 1, n - l))

    for _ in range(int(input())):
        solve()

    return 0


main()
