(n, k) = map(int, input().split())
(s, p, r) = map(int, input().split())
dic = {'p': p, 'r': r, 's': s}
t = input()
ans = 0
for i in range(k):
    bef = 'a'
    for j in range(i, n, k):
        if bef == t[j]:
            bef = 'a'
        else:
            ans += dic[t[j]]
            bef = t[j]
print(ans)
