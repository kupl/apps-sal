q = int(input())
for i in range(q):
    n = int(input())
    num = 0
    while n % 2 == 0:
        num += 1
        n //= 2
    while n % 3 == 0:
        num += 2
        n //= 3
    while n % 5 == 0:
        num += 3
        n //= 5
    if n == 1:
        print(num)
    else:
        print(-1)
