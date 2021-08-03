n = int(input())
x = [int(input()) for i in range(5)]
d = n // min(x)
if n % min(x) == 0:
    print(d + 4)
else:
    print(d + 5)
