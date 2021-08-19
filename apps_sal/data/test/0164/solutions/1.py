from math import atan, asin
(y1, y2, yw, xb, yb, r) = map(float, input().split())
x = xb * (yw - y1 - 2 * r) / (2 * yw - y1 - yb - 3 * r)
alpha = atan(x / (yw - y1 - 2 * r))
beta = asin(r / (y2 - y1 - r))
print('-1' if alpha < beta else '{0:.10f}'.format(x))
