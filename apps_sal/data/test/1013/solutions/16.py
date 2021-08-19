"""
Created on Jan 28, 2015

@author: mohamed265
"""
t = input().split()
n = int(t[0])
m = int(t[1])
slon = 9999
for i in range(n):
    t = input().split()
    for j in range(m):
        if t[j] == '1':
            if i == 0 or i == n - 1 or j == 0 or (j == m - 1):
                slon = 2
            else:
                slon = min(4, slon)
print(slon)
