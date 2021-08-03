t = int(input())
for _ in range(t):
    a, b, n, m = list(map(int, input().split()))
    if min(a, b) >= m and (a + b) >= n + m:
        print("Yes")
    else:
        print("No")
