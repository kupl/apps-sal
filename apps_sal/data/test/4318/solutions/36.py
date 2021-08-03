n = int(input())
H = list(map(int, input().split()))
h = 0
ans = 0
for i in range(n):
    if H[i] >= h:
        ans += 1
    h = max(h, H[i])
print(ans)
