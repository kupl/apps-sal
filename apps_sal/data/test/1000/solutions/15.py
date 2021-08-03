a, b = list(map(int, input().split()))
if b >= a - 1:
    print(a - 1)
else:
    summ = b
    k = a - b
    for i in range(2, k + 1):
        summ += i
    print(summ)
