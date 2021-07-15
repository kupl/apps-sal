from math import ceil
n,k = list(map(int,input().split()))
print(ceil(n*2/k)+ceil(n*5/k)+ceil(n*8/k))

