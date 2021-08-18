
import sys


class ADivideIt:
    def solve(self):
        for _ in range(int(input())):
            n = int(input())
            cnt = 0
            while n != 1:
                if n % 2 == 0:
                    n //= 2
                elif n % 3 == 0:
                    n //= 3
                    n *= 2
                elif n % 5 == 0:
                    n *= 4
                    n //= 5
                else:
                    print(-1)
                    break
                cnt += 1
            else:
                print(cnt)


solver = ADivideIt()
input = sys.stdin.readline

solver.solve()
