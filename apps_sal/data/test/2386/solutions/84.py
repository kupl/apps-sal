n = int(input())
A = list(map(int,input().split()))
B = []
for i in range(n):
    B.append(A[i]-(i+1))
B.sort()

if len(B)%2:
    ans = 0
    for i in range(n):
        ans += abs(B[i]-B[len(B)//2])
else:
    ans = float("inf")
    tmp = 0
    for i in range(n):
        tmp += abs(B[i]-B[len(B)//2-1])
    ans = min(ans, tmp)
    tmp = 0
    for i in range(n):
        tmp += abs(B[i]-B[len(B)//2])
    ans = min(ans, tmp)

print(ans)
