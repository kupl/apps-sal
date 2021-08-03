N, K = map(int, input().split())
ans = list()
for i in range(K):
    D = int(input())
    L = list(map(int, input().split()))
    ans += L
    ans = list(set(ans))
print(N - len(ans))
