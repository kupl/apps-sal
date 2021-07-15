import sys
N = int(input())
lsH = list(map(int,input().split()))
for i in range(N-2,-1,-1):
    if lsH[i] <= lsH[i+1]:
        continue
    elif lsH[i] - lsH[i+1] == 1:
        lsH[i] -= 1
    else:
        print('No')
        return
print('Yes')

