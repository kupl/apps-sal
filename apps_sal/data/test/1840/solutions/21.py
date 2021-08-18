s, b = list(map(int, input().split(" ")))
y = list(map(int, input().split()))
c = []
for i in range(b):
    d, g = list(map(int, input().split(' ')))
    c.append([d, g])

c = sorted(c)

c2 = []
j = s1 = 0
while j < b:
    s1 = s1 + c[j][1]
    c2.append(s1)
    j += 1

c2.append(0)
count = []

for i in range(s):

    start = 0
    end = b - 1
    mid = (start + end) // 2
    while start <= end:
        if c[mid][0] <= y[i]:
            start = mid + 1
            end = end
            mid = (start + end) // 2
        else:
            start = start
            end = mid - 1
            mid = (start + end) // 2
    count.append(c2[end])


print(*count)
