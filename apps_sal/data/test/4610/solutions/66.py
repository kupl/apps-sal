import collections
N, K = list(map(int, input().split()))
N_List = list(map(int, input().split()))

Chou_List = collections.Counter(N_List)
if len(Chou_List) <= K:
    print((0))
else:
    Chou_List = sorted(list(Chou_List.values()), reverse=True)
    print((sum(Chou_List[K:])))
