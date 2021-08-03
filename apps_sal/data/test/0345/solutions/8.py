import itertools
n, m = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append([])
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    arr[a].append(b)
    arr[b].append(a)
permuts = list(itertools.permutations(list(range(7))))
ans = 0
for i in range(len(permuts)):
    permut = permuts[i]
    was = []
    for i in range(6):
        was.append([False] * 6)
    c = 0
    for i in range(n):
        if permut[i] != 6:
            for g in range(len(arr[i])):
                if not permut[arr[i][g]] == 6:
                    if not was[permut[i]][permut[arr[i][g]]]:
                        c += 1
                        was[permut[i]][permut[arr[i][g]]] = True
                        was[permut[arr[i][g]]][permut[i]] = True
    for w in range(n):
        if permut[w] == 6:
            ams = [0] * 6
            for g in range(len(arr[w])):
                for j in range(6):
                    if not was[permut[arr[w][g]]][j]:
                        ams[j] += 1
            c += max(ams)
            break

    ans = max(ans, c)
print(ans)
