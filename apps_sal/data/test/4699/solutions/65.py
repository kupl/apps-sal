(n, k) = list(map(int, input().split()))
dl = list(map(int, input().split()))
i = n
while True:
    money = list(map(int, str(i)))
    for m in money:
        if dl.count(m) != 0:
            break
    else:
        print(i)
        break
    i += 1
