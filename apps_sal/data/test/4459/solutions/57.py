import collections

n = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)

cnt = 0
for k,v in list(c.items()):
  cnt += min(v-k,v) if v-k >=0 else v
print(cnt)

