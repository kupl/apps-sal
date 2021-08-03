t = int(input())
for _ in range(t):
    a, b, n, m = map(int, input().split(" "))
    if n + m <= a + b and min(a, b) >= m:
        print("Yes")
    else:
        print("No")
