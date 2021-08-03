N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
C = []

S = sum(A2) + A1[0]

for i in range(1, N):
    C.append(S)
    S += A1[i] - A2[i - 1]

if N != 1:
    print(max(C))
else:
    print(A1[0] + A2[0])
