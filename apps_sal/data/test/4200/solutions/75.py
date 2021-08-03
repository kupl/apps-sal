N, M = map(int, input().split())
A = [int(i) for i in input().split()]
S = 0
for i in range(N):
    S += A[i]
count = 0
for i in range(N):
    if(A[i] >= S / (4 * M)):
        count += 1
if(M <= count):
    print("Yes")
else:
    print("No")
