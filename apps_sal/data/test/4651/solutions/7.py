from sys import stdin

for _ in range(int(stdin.readline())):

    n = int(stdin.readline())
    arr = [int(x) for x in stdin.readline().split()]

    flags = [0] * n

    any = True

    while any == True:

        any = False

        for i in range(n - 1, 0, -1):

            if arr[i - 1] > arr[i] and flags[i - 1] == 0:
                any = True
                flags[i - 1] = 1
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

    for i in arr:
        print(i, end=" ")
    print()
