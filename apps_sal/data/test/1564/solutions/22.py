n = int(input())
x = input()
y = input()


ab = []
ba = []
for i, (xi, yi) in enumerate(zip(x, y), 1):
    s = xi + yi
    if s == 'ab':
        ab.append(i)
    elif s == 'ba':
        ba.append(i)

if len(ab) % 2 != len(ba) % 2:
    print(-1)
else:
    n1 = len(ab)
    n2 = len(ba)
    print(n1 // 2 + n2 // 2 + (2 if n1 % 2 == 1 else 0))
    for i in range(n1 // 2):
        print(ab[i * 2], ab[i * 2 + 1])
    for i in range(n2 // 2):
        print(ba[i * 2], ba[i * 2 + 1])
    if n1 % 2 == 1:
        print(ab[n1 - 1], ab[n1 - 1])
        print(ab[n1 - 1], ba[n2 - 1])
