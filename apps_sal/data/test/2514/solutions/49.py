from collections import Counter
n = int(input())
a = list(map(int, input().split()))
q = int(input())
ans = sum(a)
count = Counter(a)
for _ in range(q):
    (b, c) = map(int, input().split())
    count[c] += count[b]
    ans -= b * count[b]
    ans += c * count[b]
    count[b] = 0
    print(ans)
