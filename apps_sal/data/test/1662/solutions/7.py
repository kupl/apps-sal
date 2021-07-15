from collections import Counter
__author__ = 'asmn'

n=int(input())
a=Counter(list(map(int,input().split())))
keys=sorted(a.keys())

for i in range(len(keys)-2,-1,-1):
    if a[keys[i]] > 1:
        keys.append(keys[i])

print(len(keys))
print(' '.join(map(str,keys)))


