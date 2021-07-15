n = int(input())
import collections
co = collections.Counter(list(map(int,input().split())))
r = 0
for cnt in list(co.values()):
    r+=cnt-1
if r%2==0:
    print((n-r))
else:
    print((n-r-1))  

