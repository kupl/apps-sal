q = int(input())
for _ in range(q):
    n = int(input())
    if n < 4:
        print(4 - n)
    else:
        print(n % 2)
