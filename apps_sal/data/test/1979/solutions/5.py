n = int(input())
aa = list(map(int, input().split()))
aid = [0] * (n + 1)
for (i, a) in enumerate(aa):
    aid[a] = i
bb = list(map(int, input().split()))
dcount = [0] * n
for (i, b) in enumerate(bb):
    dcount[(i - aid[b]) % n] += 1
print(max(dcount))
