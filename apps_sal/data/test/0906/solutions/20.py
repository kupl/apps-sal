"""
ATSTNG's ejudge Python3 solution template
(actual solution is below)
"""

import sys
import queue
import string
import math
import itertools

try:
    import dev_act_ffc429465ab634  # empty file in directory
    DEV = True
except:
    DEV = False


def log(*s):
    if DEV:
        print('LOG', *s)


class EJudge:
    def __init__(self, problem="default", reclim=1 << 30):
        self.problem = problem
        sys.setrecursionlimit(reclim)

    def use_files(self, infile='', outfile=''):
        if infile != '':
            self.infile = open(infile)
            sys.stdin = self.infile
        if infile != '':
            self.outfile = open(outfile, 'w')
            sys.stdout = self.outfile

    def use_bacs_files(self):
        self.use_files(self.problem + '.in', self.problem + '.out')

    def get_tl(self):
        while True:
            pass

    def get_ml(self):
        tmp = [[[5] * 100000 for _ in range(1000)]]
        while True:
            tmp.append([[5] * 100000 for _ in range(1000)])

    def get_re(self):
        s = (0,)[8]

    def get_wa(self, wstr='blablalblah'):
        for _ in range(3):
            print(wstr)
        return


class IntReader:
    def __init__(self):
        self.ost = queue.Queue()

    def get(self):
        return int(self.sget())

    def sget(self):
        if self.ost.empty():
            for el in input().split():
                self.ost.put(el)
        return self.ost.get()

    def release(self):
        res = []
        while not self.ost.empty():
            res.append(self.ost.get())
        return res


###############################################################################
ej = EJudge('')
int_reader = IntReader()
fmap = lambda f, *l: list(map(f, *l))
def parse_int(): return fmap(int, input().split())
def revrange(x): return list(range(x - 1, -1, -1))


def aeq(ar, v):
    for el in ar:
        if el != v:
            return False
    return True


k = -1


h, w = 5, 1


def calcfast(h, w, k):
    if k == -1 and (h + w) & 1:
        return 0
    ans = pow(2, ((h - 1) * (w - 1)), 1000000007)
    return ans


def calc(h, w, k):
    a = [[0] * w for i in range(h)]
    ans = 0
    for mask in range(2**(h * w)):
        # print(bin(mask)[2:])
        cur_mask = mask
        for pos in range(h * w):
            a[pos // w][pos % w] = 1 if (cur_mask & 1 == 1) else -1
            cur_mask >>= 1
        rowsum, colsum = [1] * h, [1] * w
        for i in range(h):
            for j in range(w):
                rowsum[i] *= a[i][j]
                colsum[j] *= a[i][j]
        if aeq(rowsum, k) and aeq(colsum, k):
            ans += 1
            #print(rowsum, colsum)

    print('calced for ', h, w, k, '=', ans)
    return ans


'''
for h in range(2, 3):
    for w in range(1, 20):
        for k in [1, -1]:
            ans = calc(h, w, k)
            print('OK' if ans == calcfast(h,w,k) else "ERROR")
'''

h, w, k = parse_int()
print(calcfast(h, w, k) % 1000000007)
# '''
