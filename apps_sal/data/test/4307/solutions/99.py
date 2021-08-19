n = int(input())
divisor_list = []
for i in range(1, n + 1):
    if i % 2 != 0:
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        divisor_list.append(count)
print(divisor_list.count(8))
