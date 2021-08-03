from collections import Counter
with open(0) as f:
    N, *a = map(int, f.read().split())
data = [x - 1 for x in a] + [x for x in a] + [x + 1 for x in a]
ans = Counter(data).most_common(1)[0][1]
print(ans)
