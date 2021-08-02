n = int(input())
change = 1000 - n % 1000
if change == 1000:
    print(0)
else:
    print(change)
