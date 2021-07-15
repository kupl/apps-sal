n = int(input())
s = [input().split() for i in range(n)]
a = 0
b = 0
c = 0
d = 0
for i in range(n):
    if s[i][0] == 'AC':
        a += 1
    elif  s[i][0] == 'WA':
        b += 1
    elif s[i][0] == 'TLE':
        c += 1
    else:
        d += 1
print('AC x '+str(a))
print('WA x '+str(b))
print('TLE x '+ str(c))
print('RE x '+str(d))
