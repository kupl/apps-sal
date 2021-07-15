n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = A[0]
if n%2 == 0:
    ans += sum(A[1:n//2])*2
else:
    ans += sum(A[1:n//2])*2 + A[n//2]

print(ans)
