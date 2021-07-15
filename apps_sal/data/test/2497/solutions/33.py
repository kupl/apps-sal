from scipy.optimize import fmin
N = int(input())

INF = 10 ** 18
X = [[],[],[]]
Y = [[],[],[]]

for _ in range(N):
  x,y,d = input().split()
  x,y = int(x),int(y)
  if d == 'L':
    X[-1].append(x)
    Y[0].append(y)
  elif d == 'R':
    X[1].append(x)
    Y[0].append(y)
  elif d == 'U':
    Y[1].append(y)
    X[0].append(x)
  else:
    Y[-1].append(y)
    X[0].append(x)

for i in [-1,0,1]:
  X[i] = [min(X[i] + [INF]), max(X[i] + [-INF])]
  Y[i] = [min(Y[i] + [INF]), max(Y[i] + [-INF])]

def calc_width(t, X):
  left = INF
  right = -INF
  for i in [-1,0,1]:
    left = min(left, X[i][0] + i * t)
    right = max(right, X[i][1] + i * t)
  return right - left

def area(t):
  if t < 0:
    return INF
  return calc_width(t, X) * calc_width(t, Y)

xopt = fmin(area, x0 = 10**8, ftol = 10**-9, disp = False)
answer = area(xopt[0])
print(answer)

