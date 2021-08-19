N = int(input())
MAX = 10 ** 6
table = [0] * (MAX + 1)
for x in map(int, input().split()):
    table[x] += 1
for i in range(MAX + 1):
    if table[i]:
        for j in range(2 * i if table[i] == 1 else i, MAX + 1, i):
            table[j] = 0
print(sum(table))
