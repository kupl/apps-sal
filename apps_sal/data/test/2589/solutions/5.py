for t in range(int(input())):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if sum(a) % x != 0:
        print(n)
    else:
        i = 0
        while i < n and a[i] % x == 0:
            i += 1
        j = n - 1
        while j >= 0 and a[j] % x == 0:
            j -= 1
        print(max(n - i - 1, j))
