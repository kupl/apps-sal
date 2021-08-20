import itertools
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in itertools.permutations([i for i in range(n)]):
    tmp = 0
    for j in range(1, n):
        tmp += ((xy[i[j]][0] - xy[i[j - 1]][0]) ** 2 + (xy[i[j]][1] - xy[i[j - 1]][1]) ** 2) ** 0.5
    ans.append(tmp)
print(sum(ans) / len(ans))
