n = int(input())
h = list(map(int, input().split()))[::-1]
ans = "Yes"
for i in range(n - 1):
    if h[i] >= h[i + 1]:
        continue
    if h[i] < h[i + 1]:
        if h[i] == h[i + 1] - 1:
            h[i + 1] -= 1
            continue
        ans = "No"
        break
print(ans)
