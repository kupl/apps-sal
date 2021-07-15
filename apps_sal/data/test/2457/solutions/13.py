t = int(input())

for _ in range(t):
    n, a, b, c, d = [int(i) for i in input().split()]
    if (a + b) * n >= c-d and (a - b) * n <= c + d:
        print("Yes")
    else:
        print("No")

