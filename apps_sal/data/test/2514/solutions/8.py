from collections import Counter
n = int(input())
a = list(map(int, input().split()))
s = sum(a)
cnt = Counter(a)
q = int(input())
for i in range(q):
    b, c = map(int, input().split())
    s += (c - b) * cnt[b]
    cnt[b], cnt[c] = 0, cnt[c] + cnt[b]
    print(s)
