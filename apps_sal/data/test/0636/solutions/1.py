(n, k) = map(int, input().split())
L = list(map(int, input().split()))
for i in range(n):
    L[i] = (L[i], i)
L.sort()
ans = 0
A = []
ind = 0
while ind < len(L) and k >= L[ind][0]:
    ans += 1
    A.append(L[ind][1] + 1)
    k -= L[ind][0]
    ind += 1
print(ans)
for item in A:
    print(item, end=' ')
