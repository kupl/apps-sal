n = int(input())
m = (n + 1) // 2 + (n + 1) % 2
if n == 1:
    print(1)
    print(1, 1)
else:
    print(m)
    for i in range(1, m + 1):
        print(1, i)
    for i in range(2, n - m + 2):
        print(i, m)
