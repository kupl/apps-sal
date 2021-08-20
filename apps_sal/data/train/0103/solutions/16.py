for ttt in range(int(input())):
    (n, m) = list(map(int, input().split()))
    x = [0] * n
    y = [0] * m
    for i in range(n):
        l = list(map(int, input().split()))
        if 1 in l:
            x[i] = 1
        for j in range(m):
            if l[j] == 1:
                y[j] = 1
    t = min(x.count(0), y.count(0))
    print('Vivek' if t % 2 == 0 else 'Ashish')
