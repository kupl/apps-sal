n = int(input())
if n % 2 != 0:
    print(7, end="")
    n -= 3

for i in range(int(n / 2)):
    print(1, end="")
