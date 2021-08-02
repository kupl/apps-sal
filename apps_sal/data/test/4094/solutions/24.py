k = int(input())
a = 7
for i in range(k + 1):
    b = a % k
    if b == 0:
        print(i + 1)
        return
    a = b * 10 + 7
print('-1')
