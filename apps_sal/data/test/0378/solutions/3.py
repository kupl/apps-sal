(n, r) = map(int, input().split())
for i in range(1, 200):
    if i * n % 10 == r or i * n % 10 == 0:
        print(i)
        break
