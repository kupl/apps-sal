N = int(input())
A = sorted(list(map(int,input().split())),reverse=True)
ans = A[0]
for i in range(1,N//2):
    ans += 2* A[i]
if N%2 == 1:
    ans += A[N//2]
print(ans)
