n,k = map(int,input().split())
k = abs(k)
A = B = ans = 0
value = [False]*(2*n+1)
for i in range(k+2,2*n+1):
    A = i
    B = A - k
    if n+1 >= A:
        C = A-1
    else:
        AA = abs(A - 2*n - 2)
        C = AA-1
    if n+1 >= B:
        D = B-1
    else:
        BB = abs(B - 2*n - 2)
        D = BB-1
    ans += C*D
print(ans)
