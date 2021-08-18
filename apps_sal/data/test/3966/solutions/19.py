import math

n = int(input())
data = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += data[i]

ans = sum
data.sort()

for i in range(n - 1):
    ans += sum
    sum -= data[i]

print(ans)
