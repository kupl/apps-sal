from collections import defaultdict
Lineger_Dict = defaultdict(int)
N = int(input())
N_List = list(map(int, input().split()))
for i in N_List:
    Lineger_Dict[i] += 1


Rec = sorted([k for k, v in Lineger_Dict.items() if v >= 2] + [k for k, v in Lineger_Dict.items() if v >= 4])
if len(Rec) < 2:
    print(0)
else:
    print(Rec[-1] * Rec[-2])
