n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
import math
if n > k :
    min = math.ceil((n-k)/(k-1))
    print((min+1))

elif n == k :
    print((1))

