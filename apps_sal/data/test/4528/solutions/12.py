t = int(input())
for i in range(t):
    (n, s) = list(map(int, input().split()))
    print(24 * 60 - n * 60 - s)
