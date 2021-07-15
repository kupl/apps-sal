for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    flag = False
    for i in range(1, n):
        if a[i] - a[i-1] == 1:
            flag = True
    if flag:
        print(2)
    else:
        print(1)
