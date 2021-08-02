while(1):
    try:
        n, m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        tt = a[0] - 1
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                tt += n - a[i - 1] + a[i]
            else:
                tt += a[i] - a[i - 1]
        print(tt)
    except EOFError:
        break
