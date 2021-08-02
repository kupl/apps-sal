k = int(input())

for _ in range(k):
    n = int(input())

    A = input()
    B = input()

    X = []

    for i in range(n):
        if A[i] != B[i]:
            X.append(i)

    if len(X) == 0:
        print("Yes")

    elif len(X) == 2:
        x, y = X

        if A[x] == A[y] and B[y] == B[x]:
            print("Yes")
        else:
            print("No")

    else:
        print("No")
