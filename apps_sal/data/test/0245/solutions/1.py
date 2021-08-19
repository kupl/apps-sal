n = int(input())
# print(n)

l = [[int(x) for x in input().split()] for i in range(n)]

# print(l)

dx = (max([r[2] for r in l]) - min([r[0] for r in l]))
dy = (max([r[3] for r in l]) - min([r[1] for r in l]))
size = dx * dy
# print(size)

if dx == dy and sum([(r[2] - r[0]) * (r[3] - r[1]) for r in l]) == size:
    print("YES")
else:
    print("NO")
