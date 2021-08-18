n = int(input())
for i in range(n):
    a = int(input())
    k, amount = 1, 0
    while k * 10 + 1 <= a:
        k = k * 10 + 1
    for j in range(len(str(k))):
        for h in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if h * int(str(k)[:j + 1]) <= a:
                amount += 1
    print(amount)
