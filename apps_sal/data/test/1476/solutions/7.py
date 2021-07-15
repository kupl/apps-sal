n = int(input())

if n == 4:
    print(4)
    print("3 1 4 2")
else:
    a = []

    for i in range(1, n + 1, 2):
        a.append(i)

    for i in range(2, n + 1, 2):
        if abs(a[-1] - i) > 1:
            a.append(i)

    print(len(a))
    print(" ".join(map(str, a)))

