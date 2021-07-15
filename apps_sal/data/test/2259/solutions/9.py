from bisect import *
s, n = [0], input()
for i in map(int, input().split()):
    if i > s[-1]: s.append(i)
    else: s[bisect_right(s, i)] = i
    
print(len(s) - 1)
