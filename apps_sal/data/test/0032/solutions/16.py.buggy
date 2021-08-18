'''
Created on 30 dec. 2016

@author: Moldovan
'''
coord = 0
n = int(input())
for i in range(n):
    t, d = input().split()
    t = int(t)

    if d == 'North':
        coord = coord - t
    elif d == 'South':
        coord = coord + t

    if coord < 0 or coord > 20000:
        print("NO")
        return
    if coord == 0 and (d == 'East' or d == 'West'):
        print("NO")
        return
    if coord == 20000 and (d == 'East' or d == 'West'):
        print("NO")
        return

if coord == 0:
    print('YES')
else:
    print("NO")
