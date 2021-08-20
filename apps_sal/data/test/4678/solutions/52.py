import sys
N = int(input())
A = list(map(int, input().split()))
m = A[0]
count = 0
for a in A:
    if m > a:
        count += m - a
    else:
        m = a
print(count)
