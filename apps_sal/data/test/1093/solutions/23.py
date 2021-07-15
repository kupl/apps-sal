n,m = list(map(int,input().split()))
A = [list(input()) for i in range(n)]
p = 0
s = 0
b = 0
B =[]
for i in range(m):
    for j in range(n):
        if A[j][i] == '*':
            b += 1
    B.append(b)
    b = 0
for i in range(m-1):
    if B[i] > B[i+1] and (B[i] - B[i+1]) > s: 
        s = B[i] - B[i+1]
    elif B[i] < B[i+1] and (B[i+1] - B[i]) > p:
        p = B[i+1] - B[i]
print(p,s)









