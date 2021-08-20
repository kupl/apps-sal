N = int(input())
(D, X) = map(int, input().split())
A = []
for n in range(N):
    buff = int(input())
    A.append(buff)
div = 0
for n in range(N):
    if A[n] == 1:
        div += (D - 1) // A[n]
    elif D % A[n] == 0:
        div += (D - 1) // A[n]
    else:
        div += D // A[n]
goukei = X + div + N
print(goukei)
