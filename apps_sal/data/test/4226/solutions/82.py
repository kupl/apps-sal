x, y = map(int, input().split())
n = "No"
for i in range(51):
    for j in range(26):
        if 2 * i + 4 * j == y:
            if i + j == x:
                n = "Yes"
print(n)
