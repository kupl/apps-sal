A, B, C = map(int, input().split())
if(A == B):
    if(A != C):
        print("Yes")
        return
if(A == C):
    if(A != B):
        print("Yes")
        return
if(B == C):
    if(A != B):
        print("Yes")
        return
print("No")
