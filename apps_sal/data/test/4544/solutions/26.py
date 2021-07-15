
N = int(input())
l = list(map(int,input().split()))

flag = [0] * (max(l)+2)

minone = 0
for i in l:
    if i == 0:
        minone+= 1
    else:
        flag[i-1] += 1
    flag[i] += 1
    flag[i+1] += 1

print(max(max(flag),minone))
