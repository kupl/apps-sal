t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    tmp = n
    while(tmp % 2 == 0):
        tmp //= 2
        count += 1
    count2 = 0
    while(tmp % 3 == 0):
        tmp //= 3
        count2 += 1
    if tmp != 1:
        print(-1)

    else:
        if count > count2:
            print(-1)
        else:
            ans = count2 - count
            ans += count2
            print(ans)

