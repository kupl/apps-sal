k, x = map(int, input().split())
l = max(-1000000, x - k + 1)

for i in range(l, l + k * 2 - 1):
    print(i, end=' ')
