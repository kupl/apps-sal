q = int(input())
for i in range(q):
    n = int(input())
    if n < 4 or n == 7 or n == 5 or (n == 11):
        print(-1)
    elif n % 2 == 0:
        print(n // 4)
    else:
        print(n // 4 - 1)
