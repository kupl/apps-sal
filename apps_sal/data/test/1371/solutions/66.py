S = int(input())
l = [0, 0, 0, 1, 1, 1, 2, 3, 4]
if S <= 8:
    print(l[S])
else:
    x = 0
    for i in range(9, S + 1):
        x += l[i - 3]
        l.append(x + 4)
    print(l[S] % (10 ** 9 + 7))
