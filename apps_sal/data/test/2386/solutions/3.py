N = int(input())
A = list(map(int,input().split()))
for i in range(N):
    A[i] -= i+1
A.sort()
if len(A)%2 == 0:
    n = N//2
    am = A[n]
    ans = 0
    for i in range(N):
        ans += abs(A[i]-am)
else:
    n = (N+1)//2
    am = A[n-1]
    ans = 0
    for i in range(N):
        ans += abs(A[i]-am)
print(ans)

