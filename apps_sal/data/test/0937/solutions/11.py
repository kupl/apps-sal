t = input().split(' ')
n = int(t[0])
k = int(t[1])
A = input().split(' ')
B = input().split(' ')
for i in range(len(A)):
    A[i] = int(A[i])
    B[i] = int(B[i])
sm = 0
for i in range(len(B)):
    if B[i] == 1:
        sm += A[i]
mx = 0
for i in range(k):
    if B[i] == 0:
        mx += A[i]
cur = mx
for j in range(n-k):
    if B[j] == 0:
        cur -= A[j]
    if B[j+k] == 0:
        cur += A[j+k]
    if cur > mx:
        mx = cur
print(mx + sm)

