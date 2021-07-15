n, *h = list(map(int, open(0).read().split()))

ans = 0
i = 0
while i < n:
    j = i
    while j + 1 < n and h[j] >= h[j + 1]:
        j += 1
    ans = max(ans, j - i)
    i = j + 1
print(ans)

