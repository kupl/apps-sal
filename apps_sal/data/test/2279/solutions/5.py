import unittest
import sys


class Member:
    """ Member representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """
        it = iter(test_inputs.split('\n')) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()
        [self.n] = list(map(int, uinput().split()))
        self.nums = []
        for i in range(self.n * 2 - 1):
            self.nums.append(list(map(int, uinput().split())))
        self.pairs = []
        for i in range(len(self.nums)):
            for j in range(len(self.nums[i])):
                self.pairs.append((self.nums[i][j], i + 1, j))
        self.spairs = reversed(sorted(self.pairs))

    def calculate(self):
        """ Main calcualtion function of the class """
        result = [0] * (self.n * 2)
        paired = set()
        for p in self.spairs:
            if p[1] not in paired and p[2] not in paired:
                result[p[1]] = p[2] + 1
                result[p[2]] = p[1] + 1
                paired.add(p[1])
                paired.add(p[2])
        return str(' '.join(map(str, result)))


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Member class testing """
        test = '2\n6\n1 2\n3 4 5'
        d = Member(test)
        self.assertEqual(d.n, 2)
        self.assertEqual(d.nums[0], [6])
        self.assertEqual(d.nums[1], [1, 2])
        self.assertEqual(Member(test).calculate(), '2 1 4 3')
        test = '3\n487060\n3831 161856\n845957 794650 976977\n' + '83847 50566 691206 498447\n' + '698377 156232 59015 382455 626960'
        self.assertEqual(Member(test).calculate(), '6 5 4 3 2 1')
        test = ''
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
        d = Member(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print('\nTimelimit Test: ' + '{0:.3f}s (init {1:.3f}s calc {2:.3f}s)'.format(stop - start, calc - start, stop - calc))


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    sys.stdout.write(Member().calculate())


__starting_point()
