(l, w) = list(map(int, input().split()))
li = list(map(int, input().split()))
aa = []
tot = 0
for i in range(l - 1):
    tot += li[i]
    if i >= w:
        tot = tot - li[i - w]
    if i >= w - 1:
        aa.append(tot)
print(min(aa))
