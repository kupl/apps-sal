l = 0
for i in range(5):
    x = list(map(int, input().split()))
    if 1 in x:
        l = abs(i - 2) + abs(x.index(1) - 2)
print(l)
