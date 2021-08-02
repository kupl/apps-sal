v = int(input())
digits = [int(i) for i in input().split()]

m, ind = digits[0], 0
for i in range(1, 9):
    if digits[i] <= m:
        m, ind = digits[i], i

number = str(ind + 1) * (v // m)
l = len(number)
if l == 0:
    print(-1)
else:
    cost = l * m
    for i in range(l):
        for j in reversed(list(range(ind + 1, 9))):
            if v - cost + m >= digits[j]:
                number = number[: i] + str(j + 1) + number[i + 1:]
                cost = cost - m + digits[j]
                break

    print(number)
