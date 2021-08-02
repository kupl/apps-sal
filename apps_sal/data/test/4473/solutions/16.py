n = int(input())
Q = []
for _ in range(n):
    Q.append(list(map(int, input().split())))

for a, b, k in Q:
    y = int(k / 2)
    x = k - y
    print(a * x - b * y)
