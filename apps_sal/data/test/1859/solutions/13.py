x = int(input())
for a in range(2, 10**6):
    if (x % a == 0):
        print(1 + (x - a) // 2)
        return
print(1)
