X, Y = map(int, input().split())
result = "No"
for i in range(0, 100):
    for j in range(0, 100):
        if i + j == X and i * 2 + j * 4 == Y:
            result = "Yes"
print(result)
