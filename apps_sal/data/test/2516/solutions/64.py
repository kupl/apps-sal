N, P = map(int, input().split())
S = input()
list = [0 for _ in range(P)]
list[0] = 1
now = 0
a = 0
if P == 2 or P == 5:
    M = len(S)
    S = reversed(S)
    l = 0
    for s in S:
        if int(s) % P == 0:
            a += M - l
            l += 1
        else:
            l += 1
    print(a)


else:
    b = 1
    h = 0
    for s in reversed(S):
        h = h + b * int(s)
        list[h % P] += 1
        b = b * 10 % P

    c = 0
    for i in range(len(list)):
        c += list[i] * (list[i] - 1) / 2
    print(int(c))
