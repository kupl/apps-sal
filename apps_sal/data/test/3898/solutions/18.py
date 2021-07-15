n = int(input())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

if a[0] != 0:
    index_b = b.index(a[0])
else:
    index_b = b.index(a[1])

for index_a in range(0,len(a)):
    if a[index_a] == 0:
        continue
    if b[index_b%len(a)] == 0:
        index_b += 1

    if a[index_a] != b[index_b%len(a)]:
        print('NO')
        return
    index_b += 1

print('YES')

