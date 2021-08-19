"""
Created on Sun Dec  9 14:00:51 2018

@author: mach
"""
i = int(input())
l = []
for _ in range(i):
    k = list(map(int, input().strip().split()))
    l.append(k)
l.sort(key=lambda x: max(x[1:]), reverse=True)
k = max(l[0][1:])
sums = 0
for i in range(1, len(l)):
    j = (k - max(l[i][1:])) * (len(l[i]) - 1)
    sums += j
print(sums)
