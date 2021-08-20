(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = list(input())
i = 0
sth = []
sts = []
ans = 0
while i < n:
    if len(sts) == 0 or sts[-1] == s[i]:
        sts.append(s[i])
        sth.append(a[i])
        i += 1
    else:
        sts = []
        sth.sort(reverse=True)
        ans += sum(sth[:min(k, len(sth))])
        sth = []
sth.sort(reverse=True)
ans += sum(sth[:min(k, len(sth))])
sth = []
print(ans)
