import unittest
import sys


class Palindrom:
    """ Palindrom representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """
        it = iter(test_inputs.split('\n')) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()
        self.s = uinput()
        self.cnt = {}
        for c in self.s:
            self.cnt[c] = self.cnt.get(c, 0) + 1
        self.odd = len(self.s) % 2
        self.pcnt = dict(self.cnt)
        for i in reversed(sorted(self.pcnt)):
            if self.pcnt[i] % 2:
                self.pcnt[i] -= 1
                found = 0
                for j in sorted(self.pcnt):
                    if self.pcnt[j] % 2:
                        self.pcnt[j] += 1
                        found = 1
                        break
                if not found:
                    self.pcnt[i] += 1

    def calculate(self):
        """ Main calcualtion function of the class """
        result = []
        mid = []
        for c in sorted(self.pcnt):
            n = self.pcnt[c]
            if n > 0:
                for j in range(n // 2):
                    result.append(c)
                if n % 2:
                    mid.append(c)
        return ''.join(result + mid + list(reversed(result)))


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Palindrom class testing """
        test = 'aabc'
        d = Palindrom(test)
        self.assertEqual(d.cnt['c'], 1)
        self.assertEqual(d.pcnt['c'], 0)
        self.assertEqual(Palindrom(test).calculate(), 'abba')
        test = 'aabcd'
        self.assertEqual(Palindrom(test).calculate(), 'abcba')
        test = 'aabbcccdd'
        self.assertEqual(Palindrom(test).calculate(), 'abcdcdcba')
        test = ''

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit
        test = str(nmax) + ' ' + str(nmax) + '\n'
        numnums = [str(i) + ' ' + str(i + 1) for i in range(nmax)]
        test += '\n'.join(numnums) + '\n'
        nums = [random.randint(1, 10000) for i in range(nmax)]
        test += ' '.join(map(str, nums)) + '\n'
        start = timeit.default_timer()
        d = Palindrom(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print('\nTimelimit Test: ' + '{0:.3f}s (init {1:.3f}s calc {2:.3f}s)'.format(stop - start, calc - start, stop - calc))


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    sys.stdout.write(Palindrom().calculate())


__starting_point()
