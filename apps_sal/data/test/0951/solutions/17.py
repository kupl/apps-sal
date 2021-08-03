k = int(input())
n = input()

data = []
for c in n:
    data.append(int(c))
data.sort()

sum_digits = sum(data)
if sum_digits >= k:
    print(0)
else:
    count = 0
    for i in data:
        sum_digits += (9 - i)
        count += 1
        if sum_digits >= k:
            break
    print(count)
