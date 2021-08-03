a = int(input())
for i in range(a):
    n = int(input())
    count = 0
    while(n % 6 == 0):
        n = n // 6
        count += 1
    if(n == 1):
        print(count)
        continue
    else:
        while(n % 3 == 0):
            n = n // 3
            count += 2
        if(n == 1):
            print(count)
        else:
            print(-1)
