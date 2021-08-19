for _ in range(int(input())):
    n = int(input())
    a = list(sorted(map(int, input().split())))
    b = []
    for i in range(0, len(a), 2):
        if a[i + 1] != a[i]:
            print('NO')
            break
        b.append(a[i])
    else:
        s = b[0] * b[-1]
        for j in range(1, len(a) // 2):
            if b[j] * b[-j - 1] != s:
                print('NO')
                break
        else:
            print('YES')
