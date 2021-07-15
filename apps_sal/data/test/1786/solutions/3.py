w, h, n = map(int, input().split())

x = [0, w]
y = [0, h]
rev = []

for _ in range(n):
    s, d = input().split()
    if s == 'H':
        y.append(int(d))
    else:
        x.append(int(d))
    rev.append((s, int(d)))

x.sort()
y.sort()

_max = 0
if len(x) > 1:
    for idx in range(len(x) - 1):
        _max = max(_max, x[idx + 1] - x[idx])
else:
    _max = w
max_x = _max

_max = 0
if len(y) > 1:
    for idx in range(len(y) - 1):
        _max = max(_max, y[idx + 1] - y[idx])
else:
    _max = w
max_y = _max

enum_x = {num : idx for idx, num in enumerate(x)}
enum_y = {num : idx for idx, num in enumerate(y)}

old_x = x
old_y = y

x = [[0, 0, 0]] * len(old_x)
y = [[0, 0, 0]] * len(old_y)

for idx in range(1, len(x) - 1):
    x[idx] = [old_x[idx], idx-1, idx+1]
for idx in range(1, len(y) - 1):
    y[idx] = [old_y[idx], idx-1, idx+1]

x[-1] = [w, 0, 0]
y[-1] = [h, 0, 0]

rev.reverse()
ans = [max_x * max_y]
for item in rev:
    if item[0] == 'H':
        elem = y[enum_y[item[1]]]
        max_y = max(max_y, y[elem[2]][0] - y[elem[1]][0])
        y[elem[1]][2] = elem[2]
        y[elem[2]][1] = elem[1]
    else:
        elem = x[enum_x[item[1]]]
        max_x = max(max_x, x[elem[2]][0] - x[elem[1]][0])
        x[elem[1]][2] = elem[2]
        x[elem[2]][1] = elem[1]
    ans.append(max_x * max_y)
ans.pop()
print('\n'.join(map(str, reversed(ans))))
