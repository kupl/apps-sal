T = int(input())

for t in range(T):
    N = int(input())
    A = [int(_) for _ in input().split()]
    badE, badO = 0, 0
    for i, el in enumerate(A):
        if el%2 != i%2:
            if i%2:
                badO += 1
            else:
                badE += 1
    if badO != badE:
        print(-1)
    else:
        print(badO)

