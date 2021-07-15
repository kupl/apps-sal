N = int(input())
lists = []
for _ in range(1, N + 1):
    lists.append(int(input()))

sums = 0

for i in range(0, N):
    sums += lists[i]

sums -= int(max(lists) / 2)

print(sums)
