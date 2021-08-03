t = int(input())
for i in range(t):
    n, a, b, c, d = map(int, input().split())
    if n * (a + b) >= c - d and n * (a - b) <= c + d:
        print("Yes")
    else:
        print("No")
