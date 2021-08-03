n, x, y = map(int, input().split())
lis = [0] * n
x -= 1
y -= 1

for i in range(n):
    for j in range(i + 1, n):
        t = min(abs(i - j), abs(i - x) + abs(j - y) + 1, abs(i - y) + abs(j - x) + 1)
        lis[t] += 1

for i in range(1, n):
    print(lis[i])
