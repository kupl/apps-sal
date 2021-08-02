from itertools import permutations as perms


def main():
    read = lambda: tuple(map(int, input().split()))
    l = read()
    for p in perms(l):
        # print(*p)
        if sum(p[:3]) == sum(p[3:]):
            return "YES"
    return "NO"


print(main())
