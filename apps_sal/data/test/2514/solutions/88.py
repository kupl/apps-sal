import collections
n = int(input())
arr = list(map(int,input().split()))
cnt = collections.defaultdict(int)
for val in arr:
    cnt[val] += 1
sums = sum(arr)
q = int(input())
for _ in range(q):
    b, c = list(map(int,input().split()))
    diff = (c-b)*(cnt[b])
    sums += diff
    print(sums)
    cnt[c] += cnt[b]
    cnt[b] = 0

