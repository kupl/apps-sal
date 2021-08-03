n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

last = 0
for e in sorted(data, key=lambda x: (x[0], x[1])):
    if e[1] >= last:
        last = e[1]
    else:
        last = e[0]
print(last)
