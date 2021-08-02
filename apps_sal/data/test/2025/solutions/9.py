q = int(input())
for i in range(q):
    n = int(input())
    os = n % 4
    ce = n // 4
    if n == 1 or n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
        print(-1)
    elif os == 0 or os == 2:
        print(ce)
    elif os == 1 or os == 3:
        print(ce - 1)
