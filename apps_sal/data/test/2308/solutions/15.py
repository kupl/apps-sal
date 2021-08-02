q = int(input())

for _ in range(q):
    x = list(input())
    y = list(input())

    i = 0

    while y[-i - 1] == '0':
        i += 1

    j = i

    while x[-i - 1] == '0':
        i += 1

    print(i - j)
