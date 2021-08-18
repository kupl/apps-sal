a = int(input())

lis = [str(i) for i in range(1, a + 1)]

count = 0
for i in lis:
    if int(len(i)) % 2 != 0:
        count += 1
print(count)
