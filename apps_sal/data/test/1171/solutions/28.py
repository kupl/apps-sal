N, K = list(map(int, input().split()))
V = list(map(int, input().split()))
Vrev = V[::-1]
ans = 0
for a in range(N + 1):
    for b in range(min(K - a, N - a) + 1):
        VV = V[:a] + Vrev[:b]
        VV.sort(reverse=True)
        for k in range(min(K - a - b, len(VV))):
            if VV[-1] < 0:
                VV.pop()
        ans = max(sum(VV), ans)
print(ans)
