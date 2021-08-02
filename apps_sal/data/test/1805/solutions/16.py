q = int(input())
for qq in range(q):
    n = int(input())
    if n <= 4:
        print(4 - n)
    else:
        print(((n + 1) // 2) * 2 - n)
