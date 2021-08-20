import sys


def main():
    (n, k) = get_ints()
    s = input()
    d = set(input().split())
    ans = 0
    curr = 0
    for i in range(len(s)):
        if s[i] in d:
            curr += 1
        else:
            ans += curr * (curr + 1) // 2
            curr = 0
    ans += curr * (curr + 1) // 2
    print(ans)


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
