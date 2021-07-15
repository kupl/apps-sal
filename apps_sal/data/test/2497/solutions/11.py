inf = float('inf')
from scipy.optimize import fmin
from collections import defaultdict
dir = {'R', 'L', 'U', 'D'}
N = int(input())
dic = defaultdict(list)
for _ in range(N):
    x, y, d = input().split()
    x, y = int(x), int(y)
    dic[d].append((x, y))
x_max = defaultdict(lambda : -inf)
x_min = defaultdict(lambda : inf)
y_max = defaultdict(lambda : -inf)
y_min = defaultdict(lambda : inf)
for d in dir:
    if dic[d]:
        dic[d].sort()
        x_max[d] = dic[d][-1][0]
        x_min[d] = dic[d][0][0]
        dic[d].sort(key = lambda x:x[1])
        y_max[d] = dic[d][-1][1]
        y_min[d] = dic[d][0][1]
def dx(t):
    return max(x_max['U'], x_max['D'], x_max['R']+t, x_max['L']-t)-min(x_min['U'], x_min['D'], x_min['R']+t, x_min['L']-t)
def dy(t):
    return max(y_max['U']+t, y_max['D']-t, y_max['R'], y_max['L'])-min(y_min['U']+t, y_min['D']-t, y_min['R'], y_min['L'])
def f(t):
    if t<0:
        return inf
    return dx(t)*dy(t)

xopt = fmin(f, x0 = 10**8, ftol = 10**-9, disp = False)
print((f(xopt[0])))












