def getKey(item):
    return item[2]


n = int(input())

li = []

for _ in range(n * 2 - 1):
    li.append([int(x) for x in input().split()])

ans = [0] * (2 * n + 5)

dict = []

for i in range(2 * n - 2, -1, -1):
    for j in range(0, i + 1):
        dict.append([i + 2, j + 1, li[i][j]])

dict = sorted(dict, key=getKey, reverse=True)

# print(dict)

for i in dict:
    if ans[i[0]] == 0 and ans[i[1]] == 0:
        ans[i[0]] = i[1]
        ans[i[1]] = i[0]

print(' '.join(map(str, ans[1:2 * n + 1])))
