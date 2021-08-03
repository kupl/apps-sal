n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))
for q in range(n):
    min1 = float('inf')
    for q1 in range(max(0, q - x - 1), q):
        min1 = min(min1, a[q1])
    for q1 in range(q + 1, min(n, q + y + 1)):
        min1 = min(min1, a[q1])
    if min1 > a[q]:
        print(q + 1)
        break
