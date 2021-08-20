(n, m) = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
s1 = 0
s2 = 0
ans = 0
i = 0
j = 0
while i < n and j < m:
    if s1 == s2 and s1 != 0:
        s1 = 0
        s2 = 0
        ans += 1
    if s1 > s2:
        s2 += l2[j]
        j += 1
    elif s2 > s1:
        s1 += l1[i]
        i += 1
    else:
        s1 += l1[i]
        s2 += l2[j]
        i += 1
        j += 1
s1 += sum(l1[i:])
s2 += sum(l2[j:])
if s1 == s2 and s1 != 0:
    ans += 1
print(ans)
