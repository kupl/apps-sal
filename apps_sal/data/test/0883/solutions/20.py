'''
Created on Jan 5, 2015

@author: mohamed265
'''
n = int(input())
t = sum([int(x) for x in input().split()])
slon = 0
for i in range(1, 6):
    if (i + t) % (n + 1) != 1:
        slon += 1
print(slon)

