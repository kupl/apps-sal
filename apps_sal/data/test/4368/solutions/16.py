(n, k) = list(map(int, input().split()))
for i in range(10 ** 9):
    if n < k ** i:
        print(i)
        break
