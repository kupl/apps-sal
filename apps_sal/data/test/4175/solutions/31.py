n = int(input())
a = [input() for _ in range(n)]
cnt = 0
aset = set()
aset.add(a[0])
for i in range(1, n):
    if a[i][0] == a[i - 1][-1] and a[i] not in aset:
        aset.add(a[i])
        cnt += 1
print('Yes' if cnt == n - 1 else 'No')
