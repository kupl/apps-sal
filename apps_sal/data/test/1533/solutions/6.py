n = int(input())
h = set()
for i in range(n):
    name = input()
    if name in h:
        print('YES')
    else:
        print('NO')
        h.add(name)
