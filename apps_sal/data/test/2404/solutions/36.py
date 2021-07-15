a = int(input())
for i in range(2, a//2 + 1):
    b = a / i
    if b.is_integer():
        print(str(i) + str(int(b)))
        break

