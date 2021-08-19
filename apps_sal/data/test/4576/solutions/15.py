a = int(input())
b = int(input())
c = int(input())
sum_ = int(input())
count = 0
for i in range(0, a + 1):
    for j in range(0, b + 1):
        for k in range(0, c + 1):
            check = 500 * i + 100 * j + 50 * k
            if check == sum_:
                count += 1
print(count)
