n = int(input())
a = list(map(int, input().split()))

fans = 0
height = [0] * n
ma = []
for m in range(n):
    minh = 0
    thisans = 0
    # increasing
    np = False
    height[m] = a[m]
    for i in range(m - 1, -1, -1):
        height[i] = height[i + 1]
        if height[i] > a[i]:
            height[i] = a[i]

    for i in range(m + 1, n):
        height[i] = height[i - 1]
        if height[i] > a[i]:
            height[i] = a[i]
    thisans = sum(height)
    # fans = max(fans, thisans)
    if thisans > fans:
        ma = height.copy()
        fans = thisans
print(*list(ma))
