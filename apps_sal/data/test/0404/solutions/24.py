b = int(input())
i = 1
sum0 = 0
while i * i <= b:
    if b % i == 0:
        if b == i * i:
            sum0 += 1
        else:
            sum0 += 2
    i += 1
print(sum0)
