n = int(input())
for i in range(n):
    a, b, c, d = list(map(int, input().split()))
    print(min(abs(c - d) + b, a - 1))

