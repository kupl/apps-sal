N = int(input())
A = int(input())
while N >= 500:
    N -= 500
if N <= A:
    print('Yes')
else:
    print('No')
