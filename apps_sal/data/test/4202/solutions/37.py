(l, r) = map(int, input().split())
x = 2018
if r - l >= 2019:
    x = 0
else:
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            if i * j % 2019 < x:
                x = i * j % 2019
print(x)
