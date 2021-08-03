import math

N, K = map(int, input().split())
A = list(map(int, input().split()))

#maxA = max(A)

# for i in range(maxA,0,-1):
#  sum = 0
#  for j in range(N):
#    sum += math.ceil(A[j]/i)-1
#  if(sum>K):
#    print(i+1)
#    break

low = 0
high = max(A)
while low <= high:
    if(high == low):
        break
    mid = (low + high) // 2
    if(mid == 0):
        break
    sum = 0
    for i in range(N):
        sum += math.ceil(A[i] / mid) - 1
    # print('low:'+str(low)+',mid:'+str(mid)+',high:'+str(high)+',sum:'+str(sum))
    if(sum > K):
        low = mid + 1
    else:
        high = mid

print(high)
