n = int(input())
(t, a) = list(map(int, input().split()))
h = [int(x) for x in input().split()]
l = [t - x * 0.006 for x in h]
mi = float('INF')
for i in range(n):
    ab = abs(a - l[i])
    if mi > ab:
        mi = ab
        ans = i + 1
print(ans)
