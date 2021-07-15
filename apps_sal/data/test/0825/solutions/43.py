n = int(input())
n1 = n
pn = []
cnt = 2
ans = 0
while cnt <= int(n ** 0.5):
    while n1 % cnt == 0:
        n1 = n1 // cnt
        pn.append(cnt)
    cnt += 1
pns = list(set(pn))
ansa = []
for i in pns:
    ansa.append(pn.count(i))
for i in ansa:
    x = 1
    while i > 0:
        i -= x
        if i < 0:
            break
        x += 1
        ans += 1
print(ans + 1 if n1 != 1 else ans)
