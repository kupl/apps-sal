n = int(input())
power = [1] * 100
for i in range(1, 100):
    power[i] = power[i - 1] * 2
answer = []
a = 99
while n > 0:
    if n >= power[a]:
        n -= power[a]
        answer.append(a + 1)
    a -= 1
print(*answer)
