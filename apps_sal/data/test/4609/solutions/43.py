import collections
n = int(input())
aa = [int(input()) for a in range(n)]

caa = collections.Counter(aa) # couter aa
cnt = 0
laa = [x[1] for x in caa.items()]
for la in laa:
  if la % 2 == 1:
    cnt += 1
print(cnt)
