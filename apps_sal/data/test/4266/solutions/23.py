(k, x) = map(int, input().split())
min = x - k + 1
max = x + k - 1
for i in range(min, max + 1):
    if i < x + k - 1:
        print(i, end=' ')
    else:
        print(i)
