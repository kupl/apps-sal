n = int(input())
c = 1
for i in range(10 ** 5):
    if i ** 2 <= n:
        c = i ** 2
    else:
        break
print(c)
