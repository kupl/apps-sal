t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-2] > n - 2:
        print(n - 2)
    else:
        print(a[-2] - 1)
