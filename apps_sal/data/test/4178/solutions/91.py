n = int(input())
h = list(map(int, input().split()))[::-1]
ans = 'Yes'
for i in range(n - 1):
    if h[i + 1] - h[i] >= 2:
        ans = 'No'
    elif h[i + 1] - h[i] == 1:
        h[i + 1] -= 1
print(ans)
