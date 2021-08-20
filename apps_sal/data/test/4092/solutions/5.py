n = int(input())
l = input().split()
li = [int(i) for i in l]
hashi = dict()
pref = 0
ans = 0
hashi[pref] = 1
for i in range(n):
    pref += li[i]
    if pref in hashi:
        ans += 1
        pref = li[i]
        hashi = dict()
        hashi[0] = 1
        hashi[pref] = 1
    else:
        hashi[pref] = 1
print(ans)
