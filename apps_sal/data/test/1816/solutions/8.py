import math

n = int(input())
f = [int(x) for x in input().split()]
l = list(sorted(enumerate(f), key = lambda x : x[1]))
s = 0
for i in range(1,n):
    s += abs(l[i][0] - l[i-1][0])
print(s)
    

