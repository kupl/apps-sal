(v1, v2) = list(map(int, input().split(' ')))
(t, d) = list(map(int, input().split(' ')))
(l1, l2) = ([], [])
for (l, v) in zip((l1, l2), (v1, v2)):
    for i in range(t):
        l.append(v + d * i)
l2 = list(reversed(l2))
split = 0
for i in range(t):
    if l2[i] <= l1[i]:
        split = i
        break
l = l1[:split] + l2[split:]
print(sum(l))
