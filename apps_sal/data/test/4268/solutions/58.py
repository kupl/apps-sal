import itertools
N, D = map(int, input().split())
N_List = [i for i in range(N)]
ND_List = []
for i in range(N):
    ND_List.append(list(map(int, input().split())))

cnt = 0
for comb in itertools.combinations(N_List, 2):
    ans = 0
    for k in range(D):
        ans += (ND_List[comb[0]][k] - ND_List[comb[1]][k])**2
    ans = ans**0.5
    if ans.is_integer():
        cnt += 1
print(cnt)
