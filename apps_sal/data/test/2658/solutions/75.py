from collections import defaultdict
N, K = list(map(int, input().split()))
N_List = list(map(int, input().split()))

N_Dict = defaultdict(int)
N_Dict[1] = 1
Pos = N_List[0]
for i in range(N):
    N_Dict[Pos] += 1
    if N_Dict[Pos] == 2:
        break
    else:
        Pos = N_List[Pos - 1]

# ループ始点がPosに入っている状態
# ループがどのくらいの長さか知りたい
CPos = Pos
flg = 0
Loop_List = [CPos]
while flg == 0:
    CPos = N_List[CPos - 1]
    if CPos != Pos:
        Loop_List.append(CPos)
    else:
        flg = 1

# ループの始点に至るまでの長さを求める
FL = len(N_Dict) - len(Loop_List)
if FL <= K:
    ans = Loop_List[(K - FL) % len(Loop_List)]
else:
    ans = list(N_Dict.keys())[K]
print(ans)
