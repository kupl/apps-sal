(w, h, k) = list(map(int, input().split()))
ans = 0
for i in range(k):
    ans += 2 * h + 2 * w - 4
    h -= 4
    w -= 4
print(ans)
