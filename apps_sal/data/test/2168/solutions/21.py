n = int(input())
a = []
maxe, counter = 0, 0

for i in range(n):
    a.append(list(map(int, input().split())))

for i in a:
    if maxe < max(i[1:]):
        maxe = max(i[1:])

for i in a:
    counter += (i[0] * (maxe - max(i[1:])))
print(counter)
