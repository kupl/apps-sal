n = int(input())
pos = 0
is_correct = True
for i in range(n):
    (d, direc) = input().split()
    d = int(d)
    if is_correct:
        if pos == 0 and direc != 'South':
            is_correct = False
        if pos == 20000 and direc != 'North':
            is_correct = False
        if direc in ('North', 'South'):
            if direc == 'North':
                pos -= d
            elif direc == 'South':
                pos += d
            if pos < 0 or pos > 20000:
                is_correct = False
is_correct = is_correct and pos == 0
if is_correct:
    print('YES')
else:
    print('NO')
