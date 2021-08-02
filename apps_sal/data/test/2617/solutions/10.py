import sys
import random
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


def main():
    inf = 10 ** 20

    t = int(input())
#    t, a, b = map(int, input().split())
#    t = 1

    for _ in range(1, t + 1):
        #    print("Case #{}: ".format(_), end = '')
        n = int(input())

        total = 1
        plus = 1
        ans = []
        while(total != n):
            if(total + plus * 2 >= n):
                ans.append(n - total - plus)
                break
            else:
                next, l, r = -1, plus, plus << 1
                while(l <= r):
                    mid = (l + r) >> 1
                    if(total + mid * 2 > n):
                        r = mid - 1
                    else:
                        next = max(next, mid)
                        l = mid + 1
                ans.append(next - plus)
                plus = next
                total += plus
        print(len(ans))
        print(' '.join(map(str, ans)))


main()
