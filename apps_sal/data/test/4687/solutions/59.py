from collections import defaultdict
N, K = list(map(int, input().split()))
N_List = defaultdict(int)
for i in range(N):
    Num, Cnt = list(map(int, input().split()))
    N_List[Num] += Cnt

N_List = sorted(list(N_List.items()), key=lambda x: x[0])

ans = 0
for Key, Value in N_List:
    ans += Value
    if ans >= K:
        print(Key)
        break
