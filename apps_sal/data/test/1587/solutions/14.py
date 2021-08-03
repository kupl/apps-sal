from collections import Counter
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    C = input()
    C_cunt = Counter(C)
    cunt_r = C_cunt['R']
    ans = 0
    for i in range(cunt_r):
        if C[i] == 'W':
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
