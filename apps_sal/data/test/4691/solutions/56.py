
n = int(input())
res = {'AC':0, 'WA':0, 'TLE':0, 'RE':0}

for i in range(n):
    res[input()] +=1

for k in res:
    print(('{} x {}'.format(k, res[k])))

