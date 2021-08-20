for _ in range(int(input())):
    (a, b, p) = list(map(int, input().split()))
    ar = list(input())
    i = len(ar) - 2
    now = ar[i]
    flag = 0
    if now == 'A':
        if p >= a:
            flag = 1
    elif p >= b:
        flag = 1
    while i >= 0 and p > 0 and (flag == 1):
        if ar[i] == now:
            i -= 1
        else:
            if ar[i + 1] == 'A':
                p -= a
            else:
                p -= b
            if ar[i] == 'A':
                if p < a:
                    break
                now = 'A'
            else:
                if p < b:
                    break
                now = 'B'
    print(i + 2)
