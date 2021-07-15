from itertools import accumulate
import collections
N,M = map(int,input().split())
A = list(map(int,input().split()))
dic = collections.defaultdict(int)
P = list(accumulate(A))
for p in P:
    dic[p%M] += 1
ans = 0
for key,val in dic.items():
    if key==0: ans += val # あまり0の時はそれ自体もカウント
    ans += val*(val-1)//2
print(ans)
