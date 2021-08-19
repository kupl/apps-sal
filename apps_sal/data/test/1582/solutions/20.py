from collections import defaultdict
n = int(input())
counter = defaultdict(int)
for x in map(str, range(1, n + 1)):
    head = x[0]
    tail = x[-1]
    counter[head, tail] += 1
ans = 0
items = list(counter.items())
for ((head, tail), cnt) in items:
    ans += cnt * counter[tail, head]
print(ans)
