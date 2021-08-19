n = int(input())
if n % 10 == 0:
    print(n)
else:
    print(int(round(n / 10)) * 10)
