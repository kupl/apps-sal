from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
s = Counter(s)
s = sorted(list(s.items()), reverse=True, key=lambda x: x[1])
max_count = max(list([x[1] for x in s]))
ans = sorted([l for l, c in s if c==max_count])

for a in ans:
    print(a)

