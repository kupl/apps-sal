t = int(input())
while t:
    (n, k) = list(map(int, input().split()))
    s = list(input())
    hyp = []
    k1 = k
    while k - 1:
        hyp.append('(')
        hyp.append(')')
        k -= 1
    ll = n // 2 - (k1 - 1)
    for i in range(ll):
        hyp.append('(')
    for i in range(ll):
        hyp.append(')')
    ans = []
    for i in range(n):
        if hyp[i] != s[i]:
            l = []
            c = 0
            for j in range(i, n):
                l.append(s[j])
                c += 1
                if s[j] == hyp[i]:
                    ans.append(i + 1)
                    ans.append(j + 1)
                    break
            k = i
            for l2 in range(c - 1, -1, -1):
                s[k] = l[l2]
                k += 1
    l3 = len(ans) // 2
    print(l3)
    j = 0
    for i in range(l3):
        print(ans[j], ans[j + 1])
        j += 2
    t -= 1
