a = []
for i in range(1, 62):
    for j in range(i):
        a.append(int('1' * (i - j) + '0' + '1' * j, base=2))
(x, y) = list(map(int, input().split()))
print(len(list([d for d in a if x <= d and d <= y])))
