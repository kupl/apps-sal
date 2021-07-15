n, p = list(map(int, input().split()))
apple = 0
operations = [input() for i in range(n)][::-1]
for i in operations:
    if len(i) == 4:
        apple *= 2
    else:
        apple = apple * 2 + 1
result = 0
while apple != 0:
    if apple % 2 == 0:
        apple //= 2
        result += p * apple
    else:
        result += (p * apple) // 2
        apple //= 2
print(result)

