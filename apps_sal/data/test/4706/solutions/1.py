def resolve():
    matrix = []
    for i in range(3):
        line = input()
        matrix.append(line)
    ans = ""
    for i in range(3):
        ans += matrix[i][i]
    print(ans)
resolve()
