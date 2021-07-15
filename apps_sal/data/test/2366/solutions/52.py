N = int(input())
A = list(map(int,input().split()))

from collections import Counter
counter = Counter(A)

from collections import defaultdict
res_dic = defaultdict(int)

base = 0
for key,n in list(counter.items()):
  res_dic[key] = (n * (n - 1) // 2, (n - 1) * (n - 2) // 2)
  base += n * (n - 1) // 2
  
for i in range(N):
  ans = base - res_dic[A[i]][0] + res_dic[A[i]][1]
  print(ans)

