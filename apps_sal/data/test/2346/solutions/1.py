n = int(input())

tree = [[] for _ in range(n)]
inf = [0] * n

for i in range(n):
    ind, f = map(int, input().split())
    inf[i] = f
    if ind != -1:
        tree[ind - 1].append(i)

flag = False

for i in range(n):
    if inf[i] == 1:
        for x in tree[i]:
            if inf[x] != 1:
                break
        else:
            flag = True
            print(i + 1, end=' ')

if not flag:
    print(-1)
