(n, k) = map(int, input().rstrip().split(' '))
S = list(input())


def Game(a, b):
    if a == b:
        win = a
    elif a == 'R':
        if b == 'S':
            win = a
        else:
            win = b
    elif a == 'S':
        if b == 'P':
            win = a
        else:
            win = b
    elif b == 'R':
        win = a
    else:
        win = b
    return win


T = S
l = len(T)
for i in range(k):
    U = T + T
    l = len(U)
    for j in range(0, l, 2):
        T[j // 2] = Game(U[j], U[j + 1])
print(T[0])
