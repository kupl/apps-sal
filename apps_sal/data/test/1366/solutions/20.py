n = int(input())
bottles = [list(map(int, input().split())) for i in range(n)]
opened = set()

for i in range(n):
    for j in range(n):
        if i != j and bottles[i][1] == bottles[j][0]:
            opened.add(j)
print(n - len(opened))

