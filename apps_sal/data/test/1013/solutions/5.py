n, m = list(map(int, input().split()))

table = []
for i in range(n):
    table.append(list(map(int, input().split())))

haveonvertical = False
haveonhorizont = False

for x in table:
    if x[0] == 1 or x[-1] == 1:
        haveonvertical = True

for y in table[0]:
    if y == 1:
        haveonhorizont = True

for y in table[-1]:
    if y == 1:
        haveonhorizont = True

if haveonhorizont or haveonvertical:
    print(2)
else:
    print(4)
