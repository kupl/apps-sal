B,A = map(int,input().split())

H = W = 100
ans = [['.#'[i//50]]*W for i in range(H)]

A -= 1
B -= 1
for i in range(10):
    k = min(A,50)
    A -= k
    for j in range(k):
        ans[i*2][j*2] = '#'
    if A==0: break
for i in range(10):
    k = min(B,50)
    B -= k
    for j in range(k):
        ans[51+i*2][j*2] = '.'
    if B==0: break

print(H,W)
for row in ans:
    print(''.join(row))
