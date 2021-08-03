try:
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    test = []
    c = brr[0]
    test.append(0)
    for i in range(n):
        if arr[i] >= c:
            test.append(i)
            c = brr[i]
    result = map(str, test)
    print(' '.join(result))
except EOFError:
    pass
