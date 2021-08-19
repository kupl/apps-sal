t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    a = sorted(a)
    print(a[len(a) // 2] - a[len(a) // 2 - 1])
