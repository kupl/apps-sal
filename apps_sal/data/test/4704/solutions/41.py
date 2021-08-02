n = int(input())
a = list(map(int, input().split()))

cumsum = [0 for _ in range(n)]
cumsum[0] = a[0]

for i in range(1, n):
    cumsum[i] = a[i] + cumsum[i - 1]

result = [0 for _ in range(n - 1)]
last = cumsum[-1]
# print(last)
for i in range(n - 1):
    result[i] = abs(last - 2 * cumsum[i])

print((min(result)))
