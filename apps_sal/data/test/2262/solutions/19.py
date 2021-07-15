# cook your dish here
# from math import * 
n =int(input())
ss = set()
l = input().split()
#print(l)
for s in l:
    ss.add(''.join(sorted(str(set(s)))))
print(len(ss))
