n = int(input())
data = []
for i in range(n):
    data.append(tuple(map(int, input().split())))

cur = 0
for i in data:
    if i[0] > cur:
        cur = i[0]
        continue
    c = cur + 1 - i[0]
    c1 = (c // i[1] + (c % i[1] > 0))
    cur = i[0] + i[1] * c1
print(cur)

