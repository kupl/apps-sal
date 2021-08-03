x = int(input())

n = (x - 1) // 11
if n * 11 + 6 >= x:
    print(n * 2 + 1)
else:
    print(n * 2 + 2)
