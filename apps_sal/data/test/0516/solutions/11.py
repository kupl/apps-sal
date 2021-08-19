string = input()
numbers = string.split(' ')
a = int(numbers[0])
b = int(numbers[1])
s = input()
t = input()
values = []
lists = []
for x in range(b - a + 1):
    substring = t[x:x + a]
    n = 0
    positions = []
    for y in range(a):
        p = substring[y]
        q = s[y]
        if p != q:
            positions.append(str(y + 1))
            n += 1
    values.append(n)
    lists.append(positions)
minimum = min(values)
print(minimum)
print(' '.join(lists[values.index(minimum)]))
