n = int(input())
l = sorted(map(int, input().split()))
res = 0
i = 0
while i < n:
    j = i + 1
    while j < n and l[j] - l[i] <= 5:
        j += 1
    res = max(res, j - i)
    if j == n:
        break
    while i <= j and l[j] - l[i] > 5:
        i += 1
print(res)
