for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if [arr[0]] * n == arr:
        print(n)
    else:
        print(1)
