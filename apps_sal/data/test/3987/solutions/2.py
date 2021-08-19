input()
a = list(map(int, input().split()))
(p1, p2, p3, p4) = (0, 0, 0, 0)
for n in a:
    if n == 1:
        p1 += 1
        p3 = max(p3 + 1, p2 + 1)
    else:
        p2 = max(p2 + 1, p1 + 1)
        p4 = max(p4 + 1, p3 + 1)
print(max(p1, p2, p3, p4))
