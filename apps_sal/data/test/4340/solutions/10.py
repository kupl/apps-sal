def __starting_point():
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] -= 1
    for i in arr:
        print(i, end=" ")

__starting_point()
