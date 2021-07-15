t = int(input())
for i in range(t):
    n, a, b, c, d = list(map(int, input().split()))
    min_now = (a - b) * n
    max_now = (a + b) * n
    min_ob = c - d
    max_ob = c + d
    if min_now > max_ob or max_now < min_ob:
        print("No")
    else:
        print("Yes")

