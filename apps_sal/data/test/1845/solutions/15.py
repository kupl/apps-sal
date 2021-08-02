n = int(input())
a = list(map(int, input().split()))
su = sum(a)
a.sort()
mi = a[0]
i = 0
ma = 0
s = list(set(a))
n = len(s)
while i < n:
    j = 2
    while j < s[i]:
        if s[i] % j == 0:
            ans = (j - 1) * (int(s[i] / j) - mi)
            ma = max(ma, ans)
        j += 1
    i += 1
print(su - ma)
