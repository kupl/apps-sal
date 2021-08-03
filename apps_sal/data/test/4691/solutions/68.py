n = int(input())
a, w, t, r = 0, 0, 0, 0
for i in range(n):
    g = input()
    if g == 'AC':
        a += 1
    if g == 'WA':
        w += 1
    if g == 'TLE':
        t += 1
    if g == 'RE':
        r += 1
print('AC x ' + str(a))
print('WA x ' + str(w))
print('TLE x ' + str(t))
print('RE x ' + str(r))
