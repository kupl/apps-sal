# WeirdBugsButOkay

t = int(input())

for wqe in range(0, t):
    n = int(input())
    if n % 2 == 0:
        print(n // 2 - 1)
    else:
        print((n - 1) // 2)
