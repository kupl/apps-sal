t = int(input())
for kek in range(t):
    (n, m) = map(int, input().split())
    print(n * m % 2 + n * m // 2)
