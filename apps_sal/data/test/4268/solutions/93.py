(n, d) = map(int, input().split())
x = []
for _ in range(n):
    x.append(list(map(int, input().split())))
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if i != j:
            sum = 0
            for k in range(d):
                sum += (x[i][k] - x[j][k]) ** 2
            if sum ** 0.5 % 1 == 0:
                count += 1
print(count)
