n = int(input())
lis = [0] + list(map(int, input().split()))

b = [0] * (n + 1)

for i in reversed(range(1, n + 1)):
    ball = 0
    base = i + 1

    for j in range(i, n + 1, i):
        ball += b[j]

    if ball % 2 != lis[i]:
        b[i] = 1

print(sum(b))
print(*[i for i, b in enumerate(b) if b == 1], sep=' ')
