n = int(input())
a = input()
b = input()
tos = []
for i in range(n):
    if i > n - i - 1:
        break
    if i == n - i - 1:
        tos.append([a[i], b[i], 'aa', 'aa'])
        break
    else:
        x = [a[i], a[n - i - 1], b[i], b[n - i - 1]]
        tos.append(x)


def nos(x):
    a = x[:2]
    b = x[2:]
    a.sort()
    b.sort()
    a = ''.join(a)
    b = ''.join(b)
    if a == b:
        return 0
    if b[0] == b[1]:
        if a[0] == a[1]:
            return 0
        else:
            return 1
    if a[0] == b[0]:
        return 1
    if a[0] == b[1]:
        return 1
    if a[1] == b[0]:
        return 1
    if a[1] == b[1]:
        return 1
    return 2


if n == 1:
    if a == b:
        print(0)
    else:
        print(1)
else:
    changes = 0
    for i in tos:
        changes += nos(i)
    print(changes)
