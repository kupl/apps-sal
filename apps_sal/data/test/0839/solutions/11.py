from itertools import permutations
matrix, ans = [list(map(int, input().split())) + [0] for x in range(5)] + [[0] * 6], 0
for perm in permutations(list(range(5))):
    x = list(perm) + [5]
    temp = 0
    for i in range(5):
        for j in range(i, 5, 2):
            temp += matrix[x[j]][x[j + 1]] + matrix[x[j + 1]][x[j]]
    ans = max(ans, temp)
print(ans)
