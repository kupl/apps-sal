from collections import deque
s = list(input())
n = int(input())
for i in range(n):
    l,r,k = map(int,input().split())
    x = deque(s[l-1:r])
    x.rotate(k)
    s[l-1:r] = x
print(''.join(map(str,s)))
