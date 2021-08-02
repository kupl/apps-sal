"""
ATSTNG's ejudge Python3 solution template
(actual solution is below)
"""
import sys
import queue

try:
    import dev_act_ffc429465ab634  # empty file in directory
    DEV = True
except:
    DEV = False


def log(*s):
    if DEV: print('LOG', *s)


class EJudge:
    def __init__(self, problem="default", reclim=1 << 30):
        self.problem = problem
        sys.setrecursionlimit(reclim)

    def use_files(self, infile='', outfile=''):
        if infile != '':
            self.infile = open(infile)
            sys.stdin = self.infile
        if outfile != '':
            self.outfile = open(outfile, 'w')
            sys.stdout = self.outfile

    def use_bacs_files(self):
        self.use_files(self.problem + '.in', self.problem + '.out')

    def get_tl(self):
        while True: pass

    def get_ml(self):
        tmp = [[[5] * 100000 for _ in range(1000)]]
        while True: tmp.append([[5] * 100000 for _ in range(1000)])

    def get_re(self):
        s = (0,)[8]

    def get_wa(self, wstr='blablalblah'):
        for _ in range(3): print(wstr)
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


def tokenized(s):
    """ Parses given string into tokens with default rules """
    word = []

    for ch in s.strip():
        if ch == ' ':
            if word: yield ''.join(word); word = []
        elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9':
            word.append(ch)
        else:
            if word: yield ''.join(word); word = []
            yield ch

    if word: yield ''.join(word); word = []


###############################################################################
ej = EJudge()
int_reader = IntReader()
fmap = lambda f, *l: list(map(f, *l))
parse_int = lambda: fmap(int, input().split())

# input
n = bin(int(input()) - 1)[2:][::-1]
log(n)
bit_full_cost = [(1 << i) * (i + 1) for i in range(100)]
bit_cost = [1 << i for i in range(100)]
log(bit_cost)
ans = 0
for i in range(len(n)):
    if n[i] == '1':
        if i > 0: ans += bit_full_cost[i - 1]
        ans += bit_cost[i]


print(ans)


'''
1 2 3 4 5 6 7 8


8 7
0 5
  0

'''
