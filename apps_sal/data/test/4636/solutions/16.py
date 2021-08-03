
t = int(input())

for loop in range(t):

    n = int(input())

    lis = list(map(int, input().split()))

    ai = 0
    bi = n - 1

    A = [0]
    B = [0]
    move = 0

    while True:

        if ai > bi:
            break

        na = 0
        while na <= B[-1]:

            if ai > bi:
                break

            na += lis[ai]
            ai += 1

        A.append(na)
        if na > 0:
            move += 1

        nb = 0
        while nb <= A[-1]:

            if ai > bi:
                break

            nb += lis[bi]
            bi -= 1
        B.append(nb)
        if nb > 0:
            move += 1

    print(move, sum(A), sum(B))
