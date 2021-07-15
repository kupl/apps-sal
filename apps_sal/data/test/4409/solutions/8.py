N = int(input())
A = [int(a) for a in input().split()]
B = [0] * (2*10**5+10)
for a in A:
    B[a] += 1
ma = 0
mai = 0
for i in range(len(B)):
    if B[i] > ma:
        ma = B[i]
        maa = i

for i in range(N):
    if A[i] == maa:
        mai = i
        break
print(N - ma)

for i in range(mai)[::-1]:
    if A[i] < maa:
        print(1, i+1, i+2)
    elif A[i] > maa:
        print(2, i+1, i+2)

for i in range(mai+1, N):
    if A[i] < maa:
        print(1, i+1, i)
    elif A[i] > maa:
        print(2, i+1, i)

