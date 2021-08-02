n = int(input())
data = list(map(int, input().split()))
ans = 1

for i in range(1, n):
    if all(data[i] >= j for j in data[0:i]):
        ans += 1
print(ans)
