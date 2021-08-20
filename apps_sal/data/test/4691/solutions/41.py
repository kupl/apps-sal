N = int(input())
(c0, c1, c2, c3) = (0, 0, 0, 0)
for i in range(N):
    r = input()
    if r == 'AC':
        c0 += 1
    elif r == 'WA':
        c1 += 1
    elif r == 'TLE':
        c2 += 1
    else:
        c3 += 1
print('AC x ' + str(c0))
print('WA x ' + str(c1))
print('TLE x ' + str(c2))
print('RE x ' + str(c3))
