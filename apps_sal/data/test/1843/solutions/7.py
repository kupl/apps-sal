t = int(input())
for i in range(t):
    n = int(input())
    sum = n * (n + 1) // 2
    j = 0
    while 2 ** j <= n:
        sum -= (2 ** j) * 2
        j += 1
    print(sum)

