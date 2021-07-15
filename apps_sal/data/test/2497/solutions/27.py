import itertools
N = int(input())
LX, LY = [], []
RX, RY = [], []
DX, DY = [], []
UX, UY = [], []

for _ in range(N):
  x,y,d = input().split()
  x,y = int(x), int(y)
  if d == 'L':
    LX.append(x)
    LY.append(y)
  elif d == 'R':
    RX.append(x)
    RY.append(y)
  elif d == 'U':
    UX.append(x)
    UY.append(y)
  else:
    DX.append(x)
    DY.append(y)

INF = 10**18
fixed_x = [min(UX + DX + [INF]), max(UX + DX + [-INF])]
fixed_y = [min(LY + RY + [INF]), max(LY + RY + [-INF])]

R_x = [min(RX + [INF]), max(RX + [-INF])]
L_x = [min(LX + [INF]), max(LX + [-INF])]
U_y = [min(UY + [INF]), max(UY + [-INF])]
D_y = [min(DY + [INF]), max(DY + [-INF])]

def calc_x(t):
  # t秒後の横幅
  right = fixed_x[1]
  left = fixed_x[0]
  for x in [R_x[1]+t, L_x[1]-t]:
    if right < x:
      right = x
  for x in [R_x[0]+t, L_x[0]-t]:
    if left > x:
      left = x
  return right - left

def calc_y(t):
  # t秒後の横幅
  right = fixed_y[1]
  left = fixed_y[0]
  for y in [U_y[1]+t, D_y[1]-t]:
    if right < y:
      right = y
  for y in [U_y[0]+t, D_y[0]-t]:
    if left > y:
      left = y
  return right - left

def area(t):
  if t < 0:
    return INF
  return calc_x(t) * calc_y(t)

from scipy.optimize import fmin
xopt = fmin(area, x0 = 10**8, ftol = 10**-9, disp = False)
answer = area(xopt[0])
print(answer)
