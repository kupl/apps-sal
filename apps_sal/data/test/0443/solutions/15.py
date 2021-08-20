def f():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    if n < 2:
        print(-1)
        return
    for i in range(n):
        if a[i] * 2 != s:
            print(1)
            print(i + 1)
            return
    print(-1)


f()
