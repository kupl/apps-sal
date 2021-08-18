

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
        n = iin()
        a = lin()
        l = 2 * n + 1
        done = [0] * (l)
        ans = []
        for i in a:
            done[i] = 1
        for i in a:
            ans.append(i)
            for j in range(i + 1, l):
                if done[j] == 0:
                    done[j] = 1
                    ans.append(j)
                    break
            else:
                print(-1)
                break
        else:
            print(*ans)


main()
