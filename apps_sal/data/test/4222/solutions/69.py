N, K = map(int, input().split())
d = []
A = []
for i in range(K) :
    d.append(int(input()))
    A.append(list(map(int,input().split())))

a = set()
ans = 0
for i in range(K) :
    for j in range(len(A[i])) :
        a.add(A[i][j])

for i in range(1,N+1):
    if i not in a :
        ans += 1
print(ans)
