def solvecase():
    return ''


def solve():
    N = int(input())
    s = input().strip()
    l = len(s)
    if N > 26:
        return -1
    count = len(set((c for c in s)))
    return l - count


def main():
    ans = solve()
    print(ans)


main()
