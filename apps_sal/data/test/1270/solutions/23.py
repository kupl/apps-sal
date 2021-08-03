n = int(input())
print(n // 2)
if (n % 2 == 1):
    print(3, end=" ")
    n -= 3
while n > 0:
    print(2, end=" ")
    n -= 2
