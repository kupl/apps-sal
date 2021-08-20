s = input()
l1 = [int(s[i]) for i in range(3)]
l2 = [int(s[3 + i]) for i in range(3)]
s1 = sum(l1)
s2 = sum(l2)
if s1 < s2:
    (l1, l2) = (l2, l1)
    (s1, s2) = (s2, s1)
l1.sort(reverse=True)
l2.sort()
ans = 0
p1 = 0
p2 = 0
while s1 > s2:
    if l1[p1] > 9 - l2[p2]:
        s1 -= l1[p1]
        p1 += 1
    else:
        s2 += 9 - l2[p2]
        p2 += 1
    ans += 1
print(ans)
