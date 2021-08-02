n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
heights = []
counter = arr[0]
for i in range(n):
    while arr[i] >= counter:
        heights.append(n - i)
        counter += 1

heights.reverse()


ans = 0
container = 0
for i in range(len(heights) - 1):
    if heights[i] + container <= k:
        container += heights[i]
    else:
        container = heights[i]
        ans += 1
if container > 0: ans += 1

print(ans)
