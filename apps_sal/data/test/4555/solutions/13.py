lst = input().split()
A = int(lst[0])
B = int(lst[1])
K = int(lst[2])

if (B - A + 1) <= 2 * K:
    for n in list(range(A, B + 1)):
        print(n)
else:
    for n in list(range(A, A + K)):
        print(n)
    for n in list(range(B - K + 1, B + 1)):
        print(n)
