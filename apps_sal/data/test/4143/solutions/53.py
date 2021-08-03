n = int(input())
a = [int(input()) for i in range(5)]
if n % min(a) == 0:
    print(4 + n // min(a))
else:
    print(5 + n // min(a))
