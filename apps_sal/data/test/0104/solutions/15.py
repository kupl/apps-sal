while True:
    n = int(input())

    A=input().split()

    for index in range(0, n):
        A[index] = int(A[index])

    S = sum(A)
    x = 0

    for index in range(0, n):
        x += A[index]

        if x*2 >= S:
            print(index+1)
            break

    break

