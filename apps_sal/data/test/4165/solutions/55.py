N = int(input())
L = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += L[i]
if max(L) < sum(L) - max(L):
    print('Yes')
else:
    print('No')
