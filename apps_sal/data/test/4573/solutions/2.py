n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    x[i] = (x[i], i)

x.sort()

answers = [x[n // 2 - 1][0]] * n

ans = x[n // 2][0]
for i in range(n // 2):
    answers[x[i][1]] = ans

for i in answers:
    print(i)
