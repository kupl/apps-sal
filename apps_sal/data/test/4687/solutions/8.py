from collections import defaultdict

N, K, *ab = list(map(int, open(0).read().split()))
cnt = defaultdict(int)

for a, b in zip(*[iter(ab)] * 2):
    cnt[a] += b
li = [(k, v) for k, v in list(cnt.items())]
li.sort()

for a, b in li:
    if K - b > 0:
        K -= b
    else:
        print(a)
        break
