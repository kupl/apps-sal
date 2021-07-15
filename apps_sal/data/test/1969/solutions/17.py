a = int(input())
lst = []
for i in range(a):
    lst.append(list(input()))
answer = 0
for i in range(1, a - 1):
    for j in range(1, a - 1):
        if lst[i][j] == lst[i - 1][j - 1] == lst[i - 1][j + 1] == lst[i + 1][j - 1] == lst[i + 1][j + 1] == 'X':
            answer += 1
print(answer)
