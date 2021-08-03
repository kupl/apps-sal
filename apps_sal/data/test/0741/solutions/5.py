from math import ceil, log
t = 1
for test in range(t):
    n, m = list(map(int, input().split()))
    arr = (list(map(int, input().split())))
    arr.append(m)
    prev = 0
    on = 0
    counter = 0
    for i in arr:
        if counter % 2 == 0:
            on += (i - prev)
        prev = i
        counter += 1
    off = m - on

    counter = 0
    ans = on
    prev = 0
    prevOn = 0
    for i in arr:
        if counter % 2 == 0:
            if i - prev != 1:
                tmp = prevOn + i - prev - 1 + m - i - (on - prevOn - (i - prev))
                if tmp > ans:
                    ans = tmp
            prevOn += i - prev
        else:
            if i - prev != 1:
                tmp = prevOn + i - prev - 1 + m - i - (on - prevOn)
                if tmp > ans:
                    ans = tmp
        prev = i
        counter += 1
    print(ans)
