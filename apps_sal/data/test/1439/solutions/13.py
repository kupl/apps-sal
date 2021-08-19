import unittest
import sys


class Modulo:
    """ Modulo representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """
        it = iter(test_inputs.split('\n')) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()
        [self.n, self.m] = list(map(int, uinput().split()))
        self.nums = list(map(int, uinput().split()))
        self.modnums = [v % self.m for v in self.nums]
        self.cnt = {}
        self.vars = {}
        for v in self.modnums:
            if v not in list(self.cnt.keys()):
                self.cnt[v] = 0
                self.vars[v] = set([])
            self.cnt[v] += 1

    def calculate(self):
        """ Main calcualtion function of the class """
        for v in list(self.vars.keys()):
            cur = v
            for j in range(self.cnt[v]):
                if cur in self.vars[v]:
                    break
                self.vars[v].add(cur)
                if cur == 0:
                    return 'YES'
                cur = (cur + v) % self.m
        cur = set([0])
        for var in list(self.vars.keys()):
            for s in set(cur):
                for v in self.vars[var]:
                    res = v + s
                    if res == self.m:
                        return 'YES'
                    cur.add(res % self.m)
        return 'NO'


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Modulo class testing """
        test = '3 5\n1 2 3 3'
        d = Modulo(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.m, 5)
        self.assertEqual(d.nums, [1, 2, 3, 3])
        self.assertEqual(Modulo(test).calculate(), 'YES')
        test = '1 6\n5'
        self.assertEqual(Modulo(test).calculate(), 'NO')
        test = '4 6\n3 1 1 3'
        self.assertEqual(Modulo(test).calculate(), 'YES')
        test = '6 6\n5 5 5 5 5 5'
        self.assertEqual(Modulo(test).calculate(), 'YES')
        test = '4 5\n1 1 1 1'
        self.assertEqual(Modulo(test).calculate(), 'NO')
        self.time_limit_test(10000)

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit
        test = str(nmax) + ' ' + str(990) + '\n'
        nums = [random.randint(2, 990) for i in range(nmax)]
        test += ' '.join(map(str, nums)) + '\n'
        start = timeit.default_timer()
        d = Modulo(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print('\nTimelimit Test: ' + '{0:.3f}s (init {1:.3f}s calc {2:.3f}s)'.format(stop - start, calc - start, stop - calc))


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    sys.stdout.write(Modulo().calculate())


__starting_point()
