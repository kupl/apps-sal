n = int(input())
statement = [[] for _ in range(n)]


for i in range(n):
    A = int(input())
    for j in range(A):
        x, y = list(map(int, input().split()))
        if y == 1:
            statement[i].append([x - 1, True])
        if y == 0:
            statement[i].append([x - 1, False])

cnt = 0
for bit in range(2**n):
    honest = []
    for i in range(n):
        if (bit >> i) & 1:
            honest.append(i)
    flag = True
    for j in range(len(statement)):
        if j in honest:
            for k in honest:
                if [j, False] in statement[k]:
                    flag = False
                    break
        else:
            for k in honest:
                if [j, True] in statement[k]:
                    flag = False
                    break

        if not flag:
            break
    if flag:
        cnt = max(cnt, len(honest))
print(cnt)
