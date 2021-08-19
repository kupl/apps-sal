N = int(input())
bonus = 0
pay = 0
for i in range(1, N + 1):
    if i % 15 == 0:
        bonus += 200
    pay += 800
sum = pay - bonus
print(sum)
