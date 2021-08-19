n = int(input())
count = 0
for i in range(n):
    (x1, y1, x2, y2) = list(map(int, input().split()))
    count += (x2 - x1 + 1) * (y2 - y1 + 1)
print(count)
