from sys import stdin, stdout
import traceback
import math
from collections import Counter


read = stdin.readline
write = stdout.write
writeln = lambda x: write(str(x) + "\n")


def reads(typ=int):
    return list(map(typ, read().split()))


class Sol:
    @classmethod
    def input(cls):
        s = cls()
        return s

    def solve(self):
        n = int(read())
        s = read().strip()
        self.s = s
        counts = [0] * 26
        for c in s:
            i = ord(c) - ord("a")
            counts[i] += 1
        for i in range(25, 0, -1):
            if counts[i] == 0:
                continue
            self.try_remove(i, counts[i])
        return n - len(self.s)

    def try_remove(self, ci, count):
        while self.try_remove_one(ci) and count:
            count -= 1

    def try_remove_one(self, ci):
        s = self.s
        ch = chr(ci + ord("a"))
        chl = chr(ci - 1 + ord("a"))
        for i, c in enumerate(s):
            if c != ch:
                continue
            if i > 0 and s[i - 1] == chl:
                self.s = s[:i] + s[i + 1 :]
                return True
            if i + 1 < len(self.s) and s[i + 1] == chl:
                self.s = s[:i] + s[i + 1 :]
                return True
        return False


def __starting_point():
    try:
        writeln(Sol.input().solve())
    except Exception as e:
        print("Got exception:", repr(e))
        print(traceback.format_exc())

__starting_point()
