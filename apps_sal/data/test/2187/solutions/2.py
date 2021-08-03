t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            s = s + a[i] - a[i + 1]
    print(s)
