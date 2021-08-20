(w, h, k) = list(map(int, input().split()))
ans = 0
i = 0
while i < k:
    ans += 2 * w
    w -= 4
    i += 1
h -= 2
i = 0
while i < k:
    ans += 2 * h
    h -= 4
    i += 1
print(ans)
