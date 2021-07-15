N = int(input())

for i in range(N):
    row = ""
    for j in range(N):
        if (i+j)%2 == 0:
            row += 'W'
        else:
            row += 'B'
    print(row)

