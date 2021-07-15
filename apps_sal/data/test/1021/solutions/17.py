n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Diff1 = [A[i]-A[i-1] for i in range(1,n)]
Diff2 = [B[i]-B[i-1] for i in range(1,n)]
Diff1.sort()
Diff2.sort()
if A[0] == B[0] and B[-1] == A[-1] and Diff1 == Diff2:
    print("Yes")
else:
    print("No")
    


