(n, k) = map(int, input().split())
listh = []
for i in range(n):
    listh.append(int(input()))
listh.sort()
ans = 10 ** 9
for i in range(n - k + 1):
    high = listh[i + k - 1] - listh[i]
    if high < ans:
        ans = high
print(ans)
