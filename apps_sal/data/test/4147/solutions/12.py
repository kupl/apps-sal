import itertools

n, *abc = map(int, input().split())
llst = [int(input()) for _ in range(n)]

ans = 10 ** 10
for abc_lst in itertools.product(range(4), repeat = n):
    tmp = 0
    labc = [[0, 0] for _ in range(3)]
    for i in range(n):
        pos = abc_lst[i]
        if pos == 3:
            continue
        labc[pos][0] += llst[i]
        labc[pos][1] += 1
    if [0, 0] in labc:
        continue
    for i in range(3):
        tmp += abs(abc[i] - labc[i][0])
        tmp += 10 * (labc[i][1] - 1)
    ans = min(ans, tmp)
print(ans)
