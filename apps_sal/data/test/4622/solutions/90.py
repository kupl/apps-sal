n = int(input())
A = list(map(int, input().split()))
res = set()
ans = "YES"
for i in range(n):
    if(A[i] in res):
        ans = "NO"
        break
    res.add(A[i])
print(ans)
