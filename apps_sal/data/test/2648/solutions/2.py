N = int(input())
A = list(map(int,input().split()))
M = len(set(A))
from math import ceil
print(N-ceil((N-M)/2)*2)
