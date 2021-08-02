from collections import defaultdict
n, k = map(int, input().split())
k = (n + 1) // 2
full = 0
odd = 0
count = defaultdict(int)
for x in range(n):
    x = int(input())
    count[x] += 1
for key, v in count.items():
    full += v // 2
    odd += v % 2

total = 0
step = min(k, full)

k -= step
total += step * 2
step = min(odd, k)

total += step
print(total)
