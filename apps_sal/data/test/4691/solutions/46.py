n = int(input())
acc = 0
wac = 0
tlec = 0
rec = 0
for i in range(n):
    s = input()
    if s == 'AC':
        acc += 1
    elif s == 'WA':
        wac += 1
    elif s == 'TLE':
        tlec += 1
    elif s == 'RE':
        rec += 1
print('AC x %d' % acc)
print('WA x %d' % wac)
print('TLE x %d' % tlec)
print('RE x %d' % rec)
