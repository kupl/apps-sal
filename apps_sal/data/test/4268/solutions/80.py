import math
n, d = map(int, input().split())
x = [[int(x) for x in input().split()]for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        sum = 0
        for a, b in zip(x[i], x[j]):
            sum += (a - b) * (a - b)
        if math.sqrt(sum).is_integer():
            cnt += 1
print(cnt)
