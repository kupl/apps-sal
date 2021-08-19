(n, k) = list(map(int, input().split(' ')))
h = list(map(int, input().split(' ')))
ans = 0
for i in range(len(h)):
    if h[i] >= k:
        ans += 1
print(ans)
