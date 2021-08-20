n = input()
l = len(n)
(n, k) = (int(n), input())
(K, d, ans) = ([], 1, 0)
while k:
    ll = l
    while ll > len(k) or int(k[-ll:]) >= n or k[-ll] == '0':
        if ll > 1:
            ll -= 1
        else:
            break
    K += [int(k[-ll:])]
    k = k[:-ll]
for x in K:
    ans += x * d
    d = d * n
print(ans)
