x = int(input())
for _ in range(x):
    a, b, c, d = map(int, input().split())
    print(max(a + b, c + d))
