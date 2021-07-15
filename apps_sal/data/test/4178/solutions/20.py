import math

N = int(input())
l = list(map(int,input().split()))

cur_max = l.pop()

flag = 1
while l:
    tmp = l.pop()
    if tmp <= cur_max+1:
        if tmp < cur_max:
            cur_max = tmp
    else:
        flag = 0
        break
if flag:
    print('Yes')
else:
    print('No')

