t = int(input())

for i in range(t):
    a, b = list(map(int, input().split()))

    last = -1
    b -= 1
    while last != a and b:
        b -= 1
        last = a
        aa = a
        maks = 0
        mini = 10
        while aa:
            mini = min(mini, aa % 10)
            maks = max(maks, aa % 10)
            aa = aa // 10

        a += mini * maks

    print(a)
