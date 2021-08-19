(n, k) = map(int, input().split())
for a in range(10 ** 9):
    if k ** a > n:
        print(a)
        break
