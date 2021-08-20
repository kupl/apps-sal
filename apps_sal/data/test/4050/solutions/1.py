from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
rec = defaultdict(list)
for j in range(n):
    for k in range(j, n):
        rec[sum(a[j:k + 1])].append((j, k))
ans = []
for k in rec.keys():
    tmp = []
    rec[k] = sorted(rec[k], key=lambda x: x[1])
    pre = -1
    for (a, b) in rec[k]:
        if pre >= a:
            continue
        else:
            tmp.append((a + 1, b + 1))
            pre = b
    if len(tmp) > len(ans):
        ans = tmp
print(len(ans))
for (a, b) in ans:
    print(a, b)
