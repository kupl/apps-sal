n = int(input())
l = []

for i in range(n):
    l.append(list(map(int, input().split())))

l.sort(key=lambda x: x[1])
count = 1
last = l[0][1]
for i in l:
    if not(i[0] <= last <= i[1]):
        last = i[1]
        count += 1
print(count)
