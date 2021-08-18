y, k, n = [int(x) for x in input().split()]
first = (y // k + 1) * k
if first > n:
    print(-1)
    return
l = []
for x in range(first, n + 1, k):
    l.append(str(x - y))
print(' '.join(l))
