"""
NTC here
"""
import sys
inp = sys.stdin.readline
def input(): return inp().strip()


flush = sys.stdout.flush


def iin(): return int(input())
def lin(): return list(map(int, input().split()))


def main():
    n, m = lin()
    a = [lin() for i in range(n)]
    a = [[a[j][i] for j in range(n)] for i in range(m)]
    ans = 0
    for i in range(m):
        dc = {}
        for j in range(n):
            x = a[i][j] - i - 1
            if x >= 0 and (x) % m == 0 and x // m < n:
                try:
                    dc[(j - x // m) % n] += 1
                except:
                    dc[(j - x // m) % n] = 1
        ch1, ch2 = 0, -1
        ch3 = n
        for i in dc:
            ch3 = min(ch3, i + n - dc[i])
        ans += min(n, ch3)
    print(ans)


main()
