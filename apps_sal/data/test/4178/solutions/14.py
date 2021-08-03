n = int(input())
h = list(map(int, input().split()))
m = h[0]
for i in range(1, n):
    m = max(m, h[i])
    if h[i] >= m - 1:
        continue
    print('No')
    return


print('Yes')
