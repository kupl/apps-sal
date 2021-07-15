N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    ans += min(L[2*i], L[2*i+1])
print(ans)
