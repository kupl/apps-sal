n, k = map(int, input().split())
s = input()
d = {}

for el in s:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1

for value in d.values():
    if value > k:
        print('NO')
        return

print('YES')
