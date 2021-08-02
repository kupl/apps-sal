import math
import sys


def mp():
    return list(map(int, input().split()))


def main():
    n, m, k, l = mp()
    ost = n - k
    need = (l + k)
    if ost < l or need > n:
        print(-1)
        return
    ans = (l + k - 1) // m + 1
    if ans * m - k >= l and ans * m <= n:
        print(ans)
    else:
        print(-1)


deb = 0
if deb:
    file = open("input.txt", "r")
    input = file.readline
else:
    input = sys.stdin.readline

main()

if deb:
    file.close()
