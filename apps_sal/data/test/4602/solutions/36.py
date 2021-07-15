import math

n = int(input())
k = int(input())
x = list(map(int,input().split()))
cnt = 0

dis = math.ceil(k/2)
for i in x:
    if i == k:
        continue
    elif i <= dis:
        cnt += i*2
    else:
        cnt += (k-i)*2
print(cnt)

