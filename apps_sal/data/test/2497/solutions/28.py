
n = int(input())

x_fix_max = None
x_fix_min = None
x_inc_max = None
x_inc_min = None
x_dec_max = None
x_dec_min = None

y_fix_max = None
y_fix_min = None
y_inc_max = None
y_inc_min = None
y_dec_max = None
y_dec_min = None

for i in range(n):
    x, y, d = [a for a in input().split()]
    if d == "R":
        if x_inc_max is None or x_inc_max < int(x):
            x_inc_max = int(x)
        if x_inc_min is None or x_inc_min > int(x):
            x_inc_min = int(x)
        if y_fix_max is None or y_fix_max < int(y):
            y_fix_max = int(y)
        if y_fix_min is None or y_fix_min > int(y):
            y_fix_min = int(y)
    if d == "L":
        if x_dec_max is None or x_dec_max < int(x):
            x_dec_max = int(x)
        if x_dec_min is None or x_dec_min > int(x):
            x_dec_min = int(x)
        if y_fix_max is None or y_fix_max < int(y):
            y_fix_max = int(y)
        if y_fix_min is None or y_fix_min > int(y):
            y_fix_min = int(y)
    if d == "U":
        if y_inc_max is None or y_inc_max < int(y):
            y_inc_max = int(y)
        if y_inc_min is None or y_inc_min > int(y):
            y_inc_min = int(y)
        if x_fix_max is None or x_fix_max < int(x):
            x_fix_max = int(x)
        if x_fix_min is None or x_fix_min > int(x):
            x_fix_min = int(x)
    if d == "D":
        if y_dec_max is None or y_dec_max < int(y):
            y_dec_max = int(y)
        if y_dec_min is None or y_dec_min > int(y):
            y_dec_min = int(y)
        if x_fix_max is None or x_fix_max < int(x):
            x_fix_max = int(x)
        if x_fix_min is None or x_fix_min > int(x):
            x_fix_min = int(x)

if x_inc_min is None:
    x_inc_min = 10 ** 10
if x_dec_min is None:
    x_dec_min = 10 ** 10
if x_fix_min is None:
    x_fix_min = 10 ** 10
if x_inc_max is None:
    x_inc_max = -10 ** 10
if x_dec_max is None:
    x_dec_max = -10 ** 10
if x_fix_max is None:
    x_fix_max = -10 ** 10
if y_inc_min is None:
    y_inc_min = 10 ** 10
if y_dec_min is None:
    y_dec_min = 10 ** 10
if y_fix_min is None:
    y_fix_min = 10 ** 10
if y_inc_max is None:
    y_inc_max = -10 ** 10
if y_dec_max is None:
    y_dec_max = -10 ** 10
if y_fix_max is None:
    y_fix_max = -10 ** 10

t_list = [0]
t_list += [-x_inc_max + x_fix_max, x_dec_max - x_fix_max, (x_dec_max - x_inc_max) / 2]
t_list += [-y_inc_max + y_fix_max, y_dec_max - y_fix_max, (y_dec_max - y_inc_max) / 2]
t_list += [-x_inc_min + x_fix_min, x_dec_min - x_fix_min, (x_dec_min - x_inc_min) / 2]
t_list += [-y_inc_min + y_fix_min, y_dec_min - y_fix_min, (y_dec_min - y_inc_min) / 2]


min_mult = None
for t in t_list:
    if t < 0:
        continue
    x_max = max(x_inc_max + t, x_fix_max, x_dec_max - t)
    x_min = min(x_inc_min + t, x_fix_min, x_dec_min - t)
    y_max = max(y_inc_max + t, y_fix_max, y_dec_max - t)
    y_min = min(y_inc_min + t, y_fix_min, y_dec_min - t)
    mult = (x_max - x_min) * (y_max - y_min)
    if min_mult is None or min_mult > mult:
        min_mult = mult
print((str(min_mult)))
