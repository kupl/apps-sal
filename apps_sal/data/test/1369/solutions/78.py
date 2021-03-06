import numpy
import scipy.optimize as s
(i, j) = numpy.loadtxt(open(0), skiprows=1).T


def f(x):
    return max((x[0] - i) ** 2 + (x[1] - j) ** 2)


print(f(s.fmin(f, (9, 9), disp=0)) ** 0.5)
