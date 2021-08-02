N = int(input())
l = []
S = 'Yes'
A = input()
W = A[-1]
l.append(A)
for i in range(N - 1):
    A = input()
    if A[0] != W or l.count(A) != 0:
        S = 'No'
        break
    l.append(A)
    W = A[-1]
print(S)
