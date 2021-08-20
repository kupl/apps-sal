(a, b) = map(int, input().split())
count = 0
for i in range(a, b + 1):
    i = str(i)
    if i[0] == i[4] and i[1] == i[3]:
        count += 1
print(count)
