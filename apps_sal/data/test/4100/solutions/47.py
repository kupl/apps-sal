n, k, q = list(map(int, input().split()))
points = [k] * n
for i in range(q):
    player = int(input())
    points[player - 1] += 1

for i in range(len(points)):
    points[i] -= q
    if points[i] > 0: print('Yes')
    else: print('No')
