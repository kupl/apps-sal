for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    if len(set(arr)) == 1:
        print(len(arr))
    else:
        print(1)

