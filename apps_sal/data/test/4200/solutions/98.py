N, M = map(int, input().split())
A = list(map(int, input().split()))
list.sort(A)
A.reverse()
if A[M-1] < sum(A)/4/M:
        print("No")
else:
        print("Yes")
