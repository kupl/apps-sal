for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] != 1:
            if i % 2:
                print('Second')
            else:
                print('First')
            break
    else:
        if n % 2:
            print('First')
        else:
            print('Second')
