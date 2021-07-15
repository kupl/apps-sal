N = int(input()) #количество островов
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.remove(0)
B.remove(0)
ind_b = B.index(A[0])
R = B[ind_b:] + B[0:ind_b]
if A == R:
    print("YES")
else:
    print("NO")

