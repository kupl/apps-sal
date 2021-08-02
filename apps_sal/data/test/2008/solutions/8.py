
n = int(input())
values = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    values.append((a, b))

values.sort(key=lambda x: x[0] - x[1], reverse=True)

diss = sum([values[i][0] * i + values[i][1] * (n - i - 1) for i in range(n)])
print(diss)
