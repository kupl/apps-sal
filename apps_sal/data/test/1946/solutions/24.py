n = int(input())
chemicals = {}
for i in range(n):
    line = [int(el) for el in input().split()]
    chemicals.update({line[0]: [line[1], 0]})
m = int(input())
for i in range(m):
    line = [int(el) for el in input().split()]
    if line[0] not in chemicals.keys():
        chemicals.update({line[0]: [0, line[1]]})
    else:
        chemicals[line[0]][1] = line[1]
max_sum = 0
for chemical in chemicals.keys():
    max_sum += max(chemicals[chemical])
print(max_sum)
