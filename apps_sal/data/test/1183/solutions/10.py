t = int(input())
for q in range(t):
    n, x = list(map(int, input().split()))
    used = [0] * 301
    a = list(map(int, input().split()))
    for i in range(n):
        used[a[i]] = 1
    i = 0
    while x >= 0:
        i += 1
        if used[i] == 0:
            x -= 1
    print(i - 1)
