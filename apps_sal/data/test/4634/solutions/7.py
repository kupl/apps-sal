for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    while a[i] == 0:
        i += 1
    j = n - 1
    while a[j] == 0:
        j -= 1
    print(a[i:j + 1].count(0))
