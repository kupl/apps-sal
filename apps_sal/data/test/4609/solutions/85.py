from collections import Counter
with open(0) as f:
    N, *A = map(int, f.read().split())
ans = sum(1 for v in Counter(A).values() if v & 1)
print(ans)
