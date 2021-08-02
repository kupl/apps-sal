n = int(input())
b = []
k = 0
ans = 'YES'
for i in range(n):
    b.append(input())
for i in range(n):
    for j in range(n):
        if j - 1 >= 0:
            if b[i][j - 1] == 'o':
                k += 1
        if j + 1 < n:
            if b[i][j + 1] == 'o':
                k += 1
        if i - 1 >= 0:
            if b[i - 1][j] == 'o':
                k += 1
        if i + 1 < n:
            if b[i + 1][j] == 'o':
                k += 1
        if k % 2 == 1:
            ans = 'NO'
print(ans)
