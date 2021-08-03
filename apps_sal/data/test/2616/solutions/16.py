for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = a.count(1)
    if c == n:
        if n % 2 == 0:
            print("Second")
        else:
            print("First")
    else:
        j = 0
        for i in range(n):
            if a[i] != 1:
                j = i
                break
        if j % 2 == 0:
            print("First")
        else:
            print("Second")
