N = int(input())
H = list(map(int, input().split()))

ans = [1 for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if H[j] > H[i]:
            ans[i] = 0
print(sum(ans))
