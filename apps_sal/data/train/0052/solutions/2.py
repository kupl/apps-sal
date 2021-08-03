n = int(input())
ai = []
num = 0
for i in range(n):
    ai += [int(input())]
ai.sort()
for i in range(n // 2):
    num += ai[n - i - 1] * ai[i] * 2
if n % 2:
    num += ai[n // 2] ** 2
print(num % 10007)
