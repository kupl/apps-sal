"""
Created on Wed Sep 30 22:35:24 2020

@author: liang
"""
"""
Created on Wed Sep 30 22:08:28 2020

@author: liang
"""


class Solve():

    def __init__(self):
        self.N = int(input())
        self.key = len(str(self.N))
    ans = 0
    tmp = list()

    def solve(self):
        if self.tmp:
            s = "".join(self.tmp)
            val = int(s)
            flag = True
            if val > self.N:
                flag = False
            if s.find("3") == -1:
                flag = False
            if s.find("5") == -1:
                flag = False
            if s.find("7") == -1:
                flag = False
            if flag:
                self.ans += 1
        if len(self.tmp) == self.key:
            return
        self.tmp.append("3")
        self.solve()
        self.tmp.pop()

        self.tmp.append("5")
        self.solve()
        self.tmp.pop()

        self.tmp.append("7")
        self.solve()
        self.tmp.pop()

    def print_ans(self):
        print(self.ans)


s = Solve()
s.solve()
s.print_ans()
