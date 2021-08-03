n = int(input())
m = []
for i in range(n):
    m.append(input())
x = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if(m[i][j] == "X" and m[i - 1][j - 1] == "X" and m[i + 1][j + 1] == "X" and m[i + 1][j - 1] == "X" and m[i - 1][j + 1] == "X"):
            x += 1
print(x)
