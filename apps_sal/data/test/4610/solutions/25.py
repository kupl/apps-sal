n, k = map(int, input().split())
A = list(map(int, input().split()))
D = dict.fromkeys(range(1, n + 1), 0)
ans = 0
for a in A:
    D[a] += 1
D = sorted(D.items(), key=lambda x: x[1])
for i in range(n - k):
    ans += D[i][1]
print(ans)
