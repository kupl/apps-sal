# AC
import sys


class Main:
    def __init__(self):
        self.buff = None
        self.index = 0

    def __next__(self):
        if self.buff is None or self.index == len(self.buff):
            self.buff = sys.stdin.readline().split()
            self.index = 0
        val = self.buff[self.index]
        self.index += 1
        return val

    def next_int(self):
        return int(next(self))

    def cal(self, s):
        if len(s) == 1:
            return s[0]
        if s[0] == 0:
            return self.cal(s[1:])
        v = 1
        for c in s:
            v *= c
        return v

    def solve(self):
        n = self.next_int()
        s = [x for x in next(self)]
        w = s.count('?')
        z = s.count('(')
        y = n - w - z
        ss = [x for x in s]
        if ss[0] == '?':
            ss[0] = '('
            z += 1
        if ss[-1] == '?':
            ss[-1] = ')'
            y += 1
        flag = (n % 2 == 0 and ss[0] != ')' and ss[-1] != '(' and z * 2 <= n and y * 2 <= n)

        c = 1
        for i in range(1, n - 1):
            if not flag:
                break
            if ss[i] == '(':
                c += 1
            elif ss[i] == ')':
                c -= 1
            elif z * 2 < n:
                ss[i] = '('
                c += 1
                z += 1
            else:
                ss[i] = ')'
                c -= 1
                y -= 1

            if c == 0:
                flag = False

        if not flag:
            print(':(')
        else:
            print(''.join(ss))


def __starting_point():
    Main().solve()


__starting_point()
