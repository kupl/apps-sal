t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    min = 0
    s = 0
    for i in range(n):
        s = s + a[i]
        if s < min:
            min = s
    print(abs(min))
