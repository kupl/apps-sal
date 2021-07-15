n = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

sum = 0
for i in range(n):
    if values[i] - costs[i] < 0:
        continue
    else:
        sum += values[i] - costs[i]

print(sum)
