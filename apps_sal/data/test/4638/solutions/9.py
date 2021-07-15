
n, c = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

T = [[0,0] for i in range(n)]
T[0][1] = c/2
for i in range(1, n):
    T[i][0] = min(T[i-1][0]+A[i-1], T[i-1][1]+B[i-1]+c/2)
    T[i][1] = min(T[i-1][0]+A[i-1]+c/2, T[i-1][1]+B[i-1])

print(" ".join([str(round(i[0])) for i in T]))
