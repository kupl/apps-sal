(n, k) = map(int, input().split())
H = []
for i in range(n):
    H.append(int(input()))
H.sort()
ans = min((H[i + k - 1] - H[i] for i in range(n - k + 1)))
print(ans)
