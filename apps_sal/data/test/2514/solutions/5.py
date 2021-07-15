from collections import Counter
n = int(input())
a = list(map(int, input().split()))
q = int(input())
res = sum(a)
cnt = Counter(a)
for _ in range(q):
    b, c = map(int, input().split())
    res = res + cnt[b]*(c - b)
    print(res)
    cnt[c] += cnt[b]
    cnt[b] = 0
