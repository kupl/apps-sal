X, K, D = map(int, input().split())

if(X < 0):
    X = -1 * X
if(K % 2 == 1):
    K -= 1
    X -= D
A = X - K * D

# if(A>=-1*D):
#  print(abs(A))
# else:
low = 0
high = K // 2
while low <= high:
    mid = (low + high) // 2
    A = X - mid * 2 * D
    # print('low:'+str(low)+',mid:'+str(mid)+',high:'+str(high)+',A:'+str(A))
    if(abs(A) <= D):
        # print(A)
        break
    elif(A > D):
        low = mid + 1
    else:
        high = mid - 1
print(abs(A))
