n = int(input())
alist = list(map(int,input().split()))
from collections import Counter
adic = Counter(alist)
count = 0
for k,v in adic.items():
  if int(k) <= v:
    count+=(v-int(k))
  else:
    count+=v
print(count)
