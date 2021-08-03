n = input()
print((1000 - int(n[-3:]) if int(n) % 1000 != 0 else 0))
