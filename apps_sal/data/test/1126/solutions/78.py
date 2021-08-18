n, x, m = list(map(int, input().split()))
firstOcc = [-1] * (m + 2)
arr = []
a = x
for i in range(m + 2):
    if firstOcc[a] != -1:
        break
    arr.append(a)
    firstOcc[a] = i
    a = a * a % m

ans = sum(arr[:min(n, firstOcc[a])])
cycleLen = len(arr) - firstOcc[a]
cycleSum = sum(arr[firstOcc[a]:])
ans += cycleSum * ((n - firstOcc[a]) // cycleLen)
leafLen = ((n - firstOcc[a]) % cycleLen)
ans += sum(arr[firstOcc[a]: firstOcc[a] + leafLen])
print(ans)
