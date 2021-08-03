t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    a.sort()
    print(a[n] - a[n - 1])
