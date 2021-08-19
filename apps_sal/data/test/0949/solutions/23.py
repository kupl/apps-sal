import unittest
import sys


class Gcd:
    """ Gcd representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """
        it = iter(test_inputs.split('\n')) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()
        [self.a, self.b] = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """
        result = 1 if self.a != self.b else self.a
        return str(result)


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Gcd class testing """
        test = '1 2'
        d = Gcd(test)
        self.assertEqual(d.a, 1)
        self.assertEqual(Gcd(test).calculate(), '1')
        test = '61803398874989484820458683436563811772030917980576 61803398874989484820458683436563811772030917980576'
        self.assertEqual(Gcd(test).calculate(), '61803398874989484820458683436563811772030917980576')
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
        d = Gcd(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print('\nTimelimit Test: ' + '{0:.3f}s (init {1:.3f}s calc {2:.3f}s)'.format(stop - start, calc - start, stop - calc))


def __starting_point():
    sys.setrecursionlimit(100000)
    if sys.argv[-1] == '-ut':
        unittest.main(argv=[' '])
    sys.stdout.write(Gcd().calculate())


__starting_point()
