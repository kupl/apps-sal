t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for j in range(1, 10):
        s = str(j)
        while int(s) <= n:
            s = s + str(j)
            count += 1
    print(count)
