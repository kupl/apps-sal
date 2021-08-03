N, M = map(int, input().split())
A = []
B = []

for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        B.append(b)
    if b == N:
        A.append(a)

if len(set(A) & set(B)) != 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
