for _ in range(int(input())):
    (n, t) = list(map(int, input().split()))
    (*arr,) = list(map(int, input().split()))
    flip = 0
    for i in range(n):
        if 2 * arr[i] > t:
            arr[i] = 1
        elif 2 * arr[i] < t:
            arr[i] = 0
        else:
            arr[i] = flip
            flip = 1 - flip
    print(*arr)
