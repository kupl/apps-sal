n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
rec = []
for i in range(n):
    if len(rec) == 0:
        rec.append(a[i])
    elif abs(rec[-1] - a[i]) < abs(rec[0] - a[i]):
        rec = [a[i]] + rec
    else:
        rec.append(a[i])
print(' '.join(map(str, rec)))
