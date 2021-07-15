n, m = input(), input()
ms = set(m)
ans = 0
for k in ms:
    if not n.__contains__(k):
        ans = -1
        break
    if n.count(k) >= m.count(k):
        ans += m.count(k)
    else:
        ans += n.count(k)
print(ans)
