from functools import cmp_to_key
n = int(input())
l = []
for i in range(n):
    l.append(input())
    
l.sort(key = cmp_to_key(lambda x,y : 1 if x+y > y+x else -1))
print(''.join(l))
