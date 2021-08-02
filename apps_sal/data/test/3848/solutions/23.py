n, p = list(map(int, input().split()))
s = ['#'] + list(input()) + ['#']
s1 = s[:]
aa = 'abcdefghijklmnopqrstuvwxyz'
ind = 0
for i in range(n, 0, -1):
    ind = aa.index(s[i]) + 1
    c = 0
    ans = 0
    while ind < p:
        if aa[ind] != s[i - 1] and aa[ind] != s[i - 2]:
            c = 1
            ans = ind
            break
        ind += 1
    if c:
        s[i] = aa[ans]
        ind = i
        break
ans = 0
p = 3
for i in range(ind + 1, n + 1):
    ans = 0
    while aa[ans % p] == s[i - 2] or aa[ans % p] == s[i - 1]:
        ans += 1
    s[i] = aa[ans % p]
if s <= s1:
    print("NO")
    return
print(''.join(s[1:-1]))
