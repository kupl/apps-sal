N, K = list(map(int, input().split()))
L = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(K):
    ans += L[i]
print(ans)
