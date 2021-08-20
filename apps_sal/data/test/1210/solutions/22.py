(n, p) = list(map(int, input().split(' ')))
l = []
r = []
for i in range(n):
    (li, ri) = list(map(int, input().split(' ')))
    l.append(li)
    r.append(ri)
ans = 0
for i in range(n):
    j = (i + 1) % n
    range1 = r[i] - l[i] + 1
    range2 = r[j] - l[j] + 1
    prob1 = r[i] // p - (l[i] - 1) // p
    prob2 = r[j] // p - (l[j] - 1) // p
    ans += 2000 * (prob1 * range2 + prob2 * range1 - prob1 * prob2) / range1 / range2
print(ans)
