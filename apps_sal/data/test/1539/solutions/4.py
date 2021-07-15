
n = int(input())
lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))
sum = 0
length_to_sum = {}
length_to_count = {}
cost_to_lengths = {}

for i in range(n):
  length, cost = lengths[i], costs[i]
  sum += cost
  length_to_sum[length] = length_to_sum.setdefault(length, 0) + cost
  length_to_count[length] = length_to_count.setdefault(length, 0) + 1
  cost_to_lengths.setdefault(cost, []).append(length)

length_set = set(lengths)
for lengths in list(cost_to_lengths.values()):
  lengths.sort()
unique_costs = list(reversed(sorted(cost_to_lengths.keys())))
best = -1

for length in length_set:
  total = sum - length_to_sum[length]
  seek = length_to_count[length] - 1
  if seek != 0:
    for cost in unique_costs:
      for x in cost_to_lengths[cost]:
        if x >= length:
          break
        total -= cost
        seek -= 1
        if seek == 0:
          break
      if seek == 0:
        break
  if best == -1 or total < best:
    best = total

print(best)

