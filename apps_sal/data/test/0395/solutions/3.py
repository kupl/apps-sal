from itertools import permutations as perms


def main():
    def read(): return tuple(map(int, input().split()))
    l = read()
    for p in perms(l):
        if sum(p[:3]) == sum(p[3:]):
            return "YES"
    return "NO"


print(main())
