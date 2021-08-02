n = int(input())
A = [0 for q in range(n)]
B = [0 for q in range(n)]
for i in range(n):
    (A[i], B[i]) = list(map(int, input().split()))
s1 = sum(A)
s2 = sum(B)
if s1 % 2 == 0 and s2 % 2 == 0:
    print(0)
elif s1 % 2 == 1 and s2 % 2 == 1:
    p = 0
    for i in range(n):
        if A[i] % 2 != B[i] % 2:
            p = 1
            break
    if p == 1:
        print(1)
    else:
        print(-1)
else:
    print(-1)
