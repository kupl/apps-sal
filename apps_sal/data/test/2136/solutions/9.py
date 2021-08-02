t = int(input())

for _ in range(t):
    n = int(input())
    arr = [input() for i in range(n)]

    a = arr[0][1]
    b = arr[1][0]
    c = arr[n - 2][n - 1]
    d = arr[n - 1][n - 2]

    if (a == b):
        ans = []
        if c == a:
            ans.append([n - 1, n])
        if d == a:
            ans.append([n, n - 1])

        print(len(ans))
        for item in ans:
            print(item[0], item[1])

    elif (c == d):
        ans = []
        if c == a:
            ans.append([1, 2])
        if c == b:
            ans.append([2, 1])

        print(len(ans))
        for item in ans:
            print(item[0], item[1])

    else:
        if (a == c) and (b == d):
            print(2)
            print(1, 2)
            print(n, n - 1)
        else:
            print(2)
            print(2, 1)
            print(n, n - 1)
