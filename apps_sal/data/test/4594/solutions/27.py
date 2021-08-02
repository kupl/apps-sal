num = int(input())

table = []
for i in range(num):
    table.append(int(input()))

setting = set(table)
print(len(setting))
