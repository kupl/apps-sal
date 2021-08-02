a = input()
b = input()

sum_a = sum(map(int, a[:len(b)]))
sum_b = sum(map(int, b))

count = 0
i = 0
while True:
    xor = (sum_a + sum_b + 1) % 2
    count += xor

    if i >= len(a) - len(b):
        break
    sum_a = sum_a + int(a[i + len(b)]) - int(a[i])
    i += 1

print(count)
