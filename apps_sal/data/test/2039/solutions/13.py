n = int(input())
data = list(map(int, input().split()))
ans = 0
for i in range(1, n - 1):
    if data[i - 1] < data[i] and data[i] > data[i + 1]:
        ans += 1
    if data[i - 1] > data[i] and data[i] < data[i + 1]:
        ans += 1
print(ans)
