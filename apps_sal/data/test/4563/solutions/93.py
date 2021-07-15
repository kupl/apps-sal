import math
N = int(input())
ta = [tuple(map(int,input().split())) for _ in range(N)]
left = ta[0][0]
right = ta[0][1]
res = left+right
for t,a in ta[1:]:
    tmp1 = (left+t-1)//t
    tmp2 = (right+a-1)//a
    buff = max(tmp1,tmp2)
    right = buff*a
    left = buff*t
print((int(right+left)))



