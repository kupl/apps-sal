L, R = map(int, input().split())
result = R * R
if R - L + 1 > 2019:
    R = L + 2018
for i in range(L, R + 1):
    for j in range(i + 1, R + 1):
        if (i * j) % 2019 < result:
            result = (i * j) % 2019
print(result)
