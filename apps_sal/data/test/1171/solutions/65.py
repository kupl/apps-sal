n, k = map(int, input().split())
targ = min(n, k)
v = list(map(int, input().split()))
"""
i…左を取る回数
j…右を取る回数
残り回数 k-(i+j)
"""
ans = -10**18
for i in range(targ + 1):
    for j in range(targ - i + 1):
        #print(i, j)
        nl = v[:i] + v[n - j:]
        nl.sort()
        # print(nl)
        tmp = sum(nl)
        for t in range(min(k - (i + j), i + j)):
            tmp = max(tmp, tmp - nl[t])
            # print("行いましたよ!")
        # print(tmp)
        ans = max(tmp, ans)
print(ans)
