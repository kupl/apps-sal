n = int(input())
h = list(map(int, input().split()))

ans = 'Yes'
m = 0
for i in range(1, n):
    m = max(m, h[i])
    if h[i] < m - 1:
        ans = 'No'
        break
print(ans)
