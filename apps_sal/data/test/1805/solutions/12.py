q = int(input())
for i in range(q):
    n = int(input())
    if n > 2:
        print(n % 2)
    else:
        print(4 - n)
