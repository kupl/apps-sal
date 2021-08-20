N = int(input())
for i in range(2, 10 ** 6):
    if N % 2 == 0:
        break
    N *= i
print(N)
