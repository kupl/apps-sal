lst = input().split()
N = int(lst[0])
K = int(lst[1])
L = input().split()
for i in range(N):
    L[i] = int(L[i])
L.sort(reverse=True)
ans = 0
for i in range(K):
    ans += L[i]
print(ans)
