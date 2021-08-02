n = int(input())
k = 0
for i in range(2, 1000):
    if n % i == 0:
        print(i, end='')
        print(n // i)
        break
