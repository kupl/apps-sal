X,Y,a,b,c = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
C.sort()

ans = 0
if X < a:
    A = A[a-X:]
if Y < b:
    B = B[b-Y:]
ans = 0
for i in range(X+Y):
    if len(A) == 0:
        A.append(0)
    if len(B) == 0:
        B.append(0)
    if len(C) == 0:
        C.append(0)
    if max(A[-1],B[-1],C[-1]) == A[-1]:
        ans += A[-1]
        A.pop()
    elif max(A[-1],B[-1],C[-1]) == B[-1]:
        ans += B[-1]
        B.pop()
    else:
        ans += C[-1]
        C.pop()
print(ans)
