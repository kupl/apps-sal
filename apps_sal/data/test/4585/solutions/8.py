x = int(input())
a = 0
for i in range(1, 10 ** 10):
    a += i
    if a >= x:
        print(i)
        break
