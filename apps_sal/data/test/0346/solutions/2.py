(n, m) = map(int, input().split())
a = list(map(int, input().split()))
nums = set(list(map(int, input().split())))
stan = []
auct = []
for i in range(len(a)):
    if i + 1 not in nums:
        stan.append(a[i])
    else:
        auct.append(a[i])
sm = sum(stan)
auct = list(reversed(sorted(auct)))
for i in range(len(auct)):
    if sm >= auct[i]:
        if sm > auct[i]:
            sm *= 2
        else:
            sm += auct[i]
    else:
        sm += auct[i]
print(sm)
