from scipy.optimize import*
_, *s = open(0).read().split()
def f(x): return max((x[0] - i)**2 + (x[1] - j)**2for i, j in zip(*[map(int, s)] * 2))


print(f(fmin(f, (9, 9), disp=0))**.5)
