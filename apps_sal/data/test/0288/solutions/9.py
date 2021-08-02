n = int(input())
if n == 2:
    print(1)
else:
    ans = 3
    oldans = 2
    count = 2
    b = 0
    while ans <= n:
        if ans == n:
            b = 1
            print(count)
            break
        else:
            oldans, ans = ans, ans + oldans
            count += 1
    if b == 0:
        print(count - 1)
