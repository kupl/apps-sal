(n, m) = map(int, input().split())
min1 = -1
for i in range(n):
    help = list(map(int, input().split()))
    min1 = max(min1, min(help))
print(min1)
