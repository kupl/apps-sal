n = int(input())


ctn = 0
for i in range(1, n + 1):
    if len(str(i)) % 2 == 1:
        ctn += 1


print(ctn)
