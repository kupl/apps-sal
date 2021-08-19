n = int(input())
q = list(map(int, input().split()))
p = [0] * n
for i in range(n - 1):
    p[i + 1] = p[i] + q[i]
min_in_p = min(p) - 1
p2 = [x - min_in_p for x in p]
if sorted(p2) == [x for x in range(1, n + 1)]:
    print(' '.join(map(str, p2)))
else:
    print(-1)
