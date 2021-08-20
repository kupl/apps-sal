(n, k, q) = map(int, input().split())
point = [k - q for _ in range(n)]
for _ in range(q):
    a = int(input())
    point[a - 1] += 1
for p in point:
    if p <= 0:
        print('No')
    else:
        print('Yes')
