from itertools import accumulate

nim = int(input())
array = list(accumulate([int(i) for i in input().split()]))
l, r = 0, 1
ans = float("inf")
for i in range(1, nim-2):
    while abs(array[i] - 2 * array[l+1]) < abs(array[i] - 2 * array[l]) and l < i - 1: l += 1
    while abs(array[-1] - 2 * array[r+1] + array[i]) < abs(array[-1] - 2 * array[r] + array[i]) and r < nim - 2: r += 1
    t = [array[l], array[i] - array[l], array[r] - array[i], array[-1] - array[r]]
    ans = min(ans, max(t) - min(t))
print(ans)
