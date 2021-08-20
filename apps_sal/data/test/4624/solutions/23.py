for i in range(int(input())):
    (n, x) = list(map(int, input().split()))
    ans = 2
    v = 1
    if n <= 2:
        print(1)
    else:
        for i in range(n - 2):
            v += 1
            ans += x
            if ans >= n:
                print(v)
                break
