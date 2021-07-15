n = int(input())
p1 = tuple(map(int, input().split()))
p2 = tuple(map(int, input().split()))
count = 0

for x in range(n - 1):
    p3 = tuple(map(int, input().split()))
    x1 = p2[0] - p1[0]
    y1 = p2[1] - p1[1]
    x2 = p3[0] - p2[0]
    y2 = p3[1] - p2[1]
    if x1 * y2 > x2 * y1:
        count += 1
    p1 = p2
    p2 = p3

print(count)

