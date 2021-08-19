n = int(input())
if n % 1000 == 0:
    change = 0
else:
    change = (int(n / 1000) + 1) * 1000 - n
print(change)
