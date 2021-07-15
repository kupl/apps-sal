from math import ceil 

t = 1#int(input())
for test in range(t):
    n,k = (list(map(int, input().split())))
    (ceil(((n*8)/k)))
    print((ceil(((n*8)/k))) + (ceil(((n*5)/k))) + (ceil(((n*2)/k))))
 





