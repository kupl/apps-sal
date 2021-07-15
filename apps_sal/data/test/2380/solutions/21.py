n, m = map(int, input().split())
aa = list(map(int, input().split()))
sa = sorted(aa)

bc = [list(map(int, input().split())) for i in range(m)]

sbc = sorted(bc, key=lambda x:x[1], reverse=True)
a = 0

for j in range(m):
    if sa[a] >= sbc[j][1]:
      break
    for i in range(a, min(a+sbc[j][0],n)):  
      if sa[i] < sbc[j][1]:
        sa[i] = sbc[j][1]
        a += 1
    if a >= n:
      break
      
print(sum(sa))
