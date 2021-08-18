for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    yes = 0
    for i in range(1, n - 1):
        if(a[i] > a[i - 1] and a[i] > a[i + 1]):
            print('YES')
            print(i - 1 + 1, i + 1, i + 2)
            yes = 1
            break
    if(yes == 0):
        print('NO')
