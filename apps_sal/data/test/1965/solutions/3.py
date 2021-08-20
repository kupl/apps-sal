for _ in range(int(input())):
    (n, x) = tuple(map(int, input().split()))
    arr = list(map(int, input().split()))
    if all((i == x for i in arr)):
        print(0)
    elif sum((i - x for i in arr)) == 0 or any((i == x for i in arr)):
        print(1)
    else:
        print(2)
