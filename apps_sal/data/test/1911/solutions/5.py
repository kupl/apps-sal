n,k = map(int,input().split())
a = list(map(int,input().split()))

if k == 1:
    print(max(a) - min(a))
    return

dif = []
for i in range(n - 1):
    dif.append(a[i + 1] - a[i])
dif = sorted(dif)
print(sum(dif[:-k + 1]))
