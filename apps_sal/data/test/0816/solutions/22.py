""" ATSTNG's ejudge Python3 solution template """
import sys
import queue

try:
    import dev_act_ffc429465ab634
    DEV = True
except:
    DEV = False


def log(*s):
    if DEV:
        print('L', list(s), sep='')


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
ej = EJudge()
int_reader = IntReader()
def fmap(f, l): return list(map(f, l))
def parse_int(): return fmap(int, input().split())


def sign(x): return (x > 0) - (x < 0)


# input
n, x = parse_int()
st = [0] * 100500
xored = [0] * 100500
for _ in range(n):
    st[int_reader.get()] += 1
for idx in range(100500):
    pair = idx ^ x
    if pair < 100500:
        xored[pair] = st[idx]

ans = 0
for idx in range(100500):
    ans += st[idx] * xored[idx]

if x == 0:
    ans -= n

print(ans // 2)
