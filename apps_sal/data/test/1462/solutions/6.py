import operator

table = {}

n, k = map(int, input().split(' '))

chain = input()

for ch in chain:
    if ch in table:
        table[ch] += 1
    else:
        table[ch] = 1

sorted_table = ((k, table[k]) for k in sorted(table, key=table.get, reverse=True))

total = 0
for key, value in sorted_table:
    total += min(k, value) * min(k, value)
    k -= value
    if k <= 0:
        break
print(total)
