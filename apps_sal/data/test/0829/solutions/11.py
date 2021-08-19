import sys


class AKeanuReeves:

    def solve(self):
        n = int(input())
        s = input()
        if s.count('0') != s.count('1'):
            print(1)
            print(s)
        else:
            print(2)
            print(s[0], s[1:])


solver = AKeanuReeves()
input = sys.stdin.readline
solver.solve()
