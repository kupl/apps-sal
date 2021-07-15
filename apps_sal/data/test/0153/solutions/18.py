n, k, m = list(map(int, input().split()))

nums = list(map(int, input().split()))

result = -1

alltime = sum(nums)

for made in range(n + 1):
    if(alltime * made > m):
        break
    currentres = (k + 1) * made
    currenttime = m - made * alltime
    available = []
    for item in nums:
        available.extend([item]*(n - made))
    available = sorted(available)
    for item in available:
        if(currenttime < item):
            break
        currenttime -= item
        currentres += 1
    result = max(result, currentres)

print(result)

