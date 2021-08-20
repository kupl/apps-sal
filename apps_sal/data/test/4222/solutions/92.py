import collections
(n, k) = map(int, input().split())
sunukes = [0] * n
for i in range(k):
    d = int(input())
    aa = list(map(int, input().split()))
    for a in aa:
        sunukes[a - 1] += 1
c = collections.Counter(sunukes)
ans = c[0]
print(ans)
