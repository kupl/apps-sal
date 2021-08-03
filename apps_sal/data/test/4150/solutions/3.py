n, k = map(int, input().split())
students = list(map(int, input().split()))
order = sorted(range(n), key=lambda x: -students[x])
neighbours = [[t - 1, t + 1] for t in range(n)]
neighbours[-1][1] = -1
turn = 0
team = [0] * n
for i in range(n):
    if team[order[i]] == 0:
        team[order[i]] = turn % 2 + 1
        left, right = neighbours[order[i]]
        for _ in range(k):
            if left != -1:
                team[left] = turn % 2 + 1
                neighbours[order[i]][0] = neighbours[left][0]
                if neighbours[left][0] != -1:
                    neighbours[neighbours[left][0]][1] = order[i]
                left = neighbours[left][0]
            if right != -1:
                team[right] = turn % 2 + 1
                neighbours[order[i]][1] = neighbours[right][1]
                if neighbours[right][1] != -1:
                    neighbours[neighbours[right][1]][0] = order[i]
                right = neighbours[right][1]
        left, right = neighbours[order[i]]
        if left != -1:
            neighbours[left][1] = right
        if right != -1:
            neighbours[right][0] = left
        turn += 1
print(*team, sep="")
