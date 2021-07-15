from math import ceil
Q = list(map(int, input().split()))
Q.sort()
A, B, C = Q
print((C-B+ceil((B-A)/2)+((B-A)%2==1)))



