K = int(input())
if K % 2 == 0 or K % 5 == 0:
    print(-1)
else:
    a = 7
    i = 0
    while True:
        if a % K == 0:
            print(i + 1)
            break
        else:
            a, i = (a * 10 + 7) % K, i + 1
