for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    a, b = 0, 0
    for elem in ar:
        if elem % 2 == 0:
            a += 1
        else:
            b += 1
    if a % 2 != b % 2:
        print('NO')
    else:
        if a % 2 == b % 2 == 0:
            print('YES')
        else:
            ans = 'NO'
            for i in range(1, n):
                if ar[i] - ar[i - 1] == 1:
                    ans = 'YES'
                    break
            print(ans)
