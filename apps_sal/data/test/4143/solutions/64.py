n = int(input())
l = [int(input()) for i in range(5)]

if n % min(l) == 0:
    print(n // min(l) + 4)
else:
    print(n // min(l) + 5)
