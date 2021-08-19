for _ in range(int(input())):
    (fr, ch) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if ch < fr:
        print(-1)
    elif fr == 2:
        print(-1)
    else:
        x = [[arr[i], i + 1] for i in range(fr)]
        x.sort()
        print(sum(arr) * 2 + (ch - fr) * (x[0][0] + x[1][0]))
        for i in range(fr):
            if i == fr - 1:
                print(1, fr)
            else:
                print(i + 1, i + 2)
        for i in range(fr, ch):
            print(x[0][1], x[1][1])
