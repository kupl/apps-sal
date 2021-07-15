n = int(input())
A = list(map(int, input().split()))
r = sum(A)-A[0]
l = A[0]
ans = abs(r-l)
for i in range(1,len(A)-1):
    r -= A[i]
    l += A[i]
    ans = min(ans, abs(l-r))
print(ans)
