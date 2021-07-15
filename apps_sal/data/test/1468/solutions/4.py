#!/usr/bin/env python3
from sys import stdin,stdout

def ri():
    return list(map(int, input().split()))

#n=int(stdin.readline())
n = int(input())

s =[]
for i in range(n):
    #s.append(input())
    s.append(stdin.readline().strip())

for i in range(n-1, 0, -1):
    if s[i-1] <= s[i]:
        continue
    else:
        mind = min(len(s[i]), len(s[i-1]))
        for j in range(mind):
            if s[i-1][j] > s[i][j]:
                s[i-1] = s[i-1][:j]
                break
        else:
            s[i-1] = s[i-1][:mind]

#for i in range(n):
#    print(s[i])
print('\n'.join(s))


