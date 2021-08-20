n = int(input())
a = []
b = []
for i in range(n):
    m = int(input())
    if m > 0:
        a.append(m)
    else:
        b.append(-m)
    last = m
sa = sum(a)
sb = sum(b)
if sa != sb:
    win = 1 if sa > sb else 2
elif a != b:
    win = 1 if a > b else 2
else:
    win = 1 if last > 0 else 2
print('first' if win == 1 else 'second')
