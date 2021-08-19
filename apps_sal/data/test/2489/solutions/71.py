import collections
n = int(input())
A = list(map(int, input().split()))
A.sort()
cnt = collections.Counter(A)
for a in A:
    if cnt[a] >= 2:
        del cnt[a]
    for j in range(2 * a, A[-1] + 1, a):
        del cnt[j]
print(len(cnt))
