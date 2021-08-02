n = int(input())
print('0' if n % 1000 == 0 else str(1000 - n % 1000))
