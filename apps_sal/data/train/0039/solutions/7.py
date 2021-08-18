

"""
NTC here
"""
import sys
inp = sys.stdin.readline
def input(): return inp().strip()


def iin(): return int(input())
def lin(): return list(map(int, input().split()))


def main():
    T = iin()
    while T:
        T -= 1
        a, b, p = lin()

        s = list(input())
        n = len(s)
        ans = []
        ch = 'D'
        for i in range(n - 1):
            if s[i] != ch:
                ch = s[i]
                x = a
                if ch == 'B':
                    x = b
                ans.append([x, i])
        l = len(ans)
        ans = ans[::-1]
        for i in range(1, l):
            ans[i][0] += ans[i - 1][0]
        ans = ans[::-1]
        for i, j in ans:
            if p >= i:
                print(j + 1)
                break
        else:
            print(n)


main()
