n, m = map(int, input().split())

count = []
for i in range(m):
    count.append([0] * 5)

for i in range(n):
    s = input()
    for j, c in enumerate(s):
        count[j]["ABCDE".index(c)] += 1

points = list(map(int, input().split()))

total = sum(point * max(c) for point, c in zip(points, count))

print(total)
