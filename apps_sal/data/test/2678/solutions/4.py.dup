t = int(input())
l = []
for i in range(t):
    l.append([int(i) for i in input().split()])
l.sort(key=lambda x: x[1])
last = l[0][1]
count = 1
for i in range(1, t):
    if l[i][0] > last:
        count += 1
        last = l[i][1]
print(count)
