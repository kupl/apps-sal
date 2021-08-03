from math import fabs
while(1):
    try:
        n = int(input())
        a = []
        for i in range(0, n):
            a.append(int(input()))
        summ = a[0] + 1
        for i in range(1, n):
            summ += fabs(a[i - 1] - a[i]) + 2
        print(int(summ))
    except EOFError:
        break
