n = int(input())
res = 1
for i in range(100000):
    if i ** 2 > n:
        break
    res = i * i
print(res)
