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


def tokenized(s):
    """ Parses given string into tokens with default rules """
    word = []

    for ch in s.strip():
        if ch == ' ':
            if word:
                yield ''.join(word)
                word = []
        elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9':
            word.append(ch)
        else:
            if word:
                yield ''.join(word)
                word = []
            yield ch

    if word:
        yield ''.join(word)
        word = []


###############################################################################
ej = EJudge()
int_reader = IntReader()
fmap = lambda f, *l: list(map(f, *l))
def parse_int(): return fmap(int, input().split())


# input
n, k = parse_int()

seq = fmap(lambda x: x == "YES", input().split())

names = [chr(ord('A') + i) for i in range(25)] + ['S' + chr(ord('a') + i) for i in range(25)]
names = names[:n]

for i in range(len(seq)):
    if not seq[i]:
        names[i + k - 1] = names[i]

print(' '.join(names))
