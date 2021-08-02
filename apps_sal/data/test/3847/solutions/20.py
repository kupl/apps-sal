n, m = list(map(int, input().split()))
l = list(map(int, input().split()))
l1 = list(map(int, input().split()))
x = int(input())
l = [0] + l
l1 = [0] + l1
for i in range(1, n + 1):
    l[i] += l[i - 1]
for j in range(1, m + 1):
    l1[j] += l1[j - 1]
# print(l,l1)
maxsum = [999999999999999999] * (n)
for i in range(1, n + 1):
    for j in range(i, n + 1):
        sum = l[j] - l[j - i]
        maxsum[i - 1] = min(maxsum[i - 1], sum)
maxsum1 = [999999999999999999] * (m)
for i in range(1, m + 1):
    for j in range(i, m + 1):
        sum = l1[j] - l1[j - i]
        maxsum1[i - 1] = min(maxsum1[i - 1], sum)
ans = 0
# print(maxsum,maxsum1)
for i in range(n):
    for j in range(m - 1, -1, -1):
        if maxsum[i] * maxsum1[j] <= x:
            ans = max(ans, (i + 1) * (j + 1))
print(ans)
