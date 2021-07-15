from collections import defaultdict
H, W, N, *L = map(int, open(0).read().split())
dic = defaultdict(int)
for a, b in zip(*[iter(L)]*2):
  for i in range(a-2,a+1):
    for j in range(b-2,b+1):
      if 0<i and i+2<=H and 0<j and j+2<=W:
        dic[(i,j)] += 1
ans = [0]*10
ans[0] = (W-2)*(H-2)
for k in dic.keys():
  ans[dic[k]] += 1
  ans[0] -= 1
print(*ans,sep='\n')
