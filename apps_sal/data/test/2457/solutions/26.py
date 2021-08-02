t = int(input())
for i in range(t):
    n, a, b, c, d = list(map(int, input().split()))
    if (a - b) * n > c + d or (a + b) * n < c - d:
        print("No")
    else:
        print("Yes")
