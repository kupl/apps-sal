ls = list(map(int, input().split()))
for j in range(ls[1]):
    if ls[0] % 10 > 0:
        ls[0] = ls[0] - 1
    else:
        ls[0] = ls[0] // 10
print(ls[0])
