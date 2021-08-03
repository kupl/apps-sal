n, n1, n2 = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
if (n2 > n1):
    n1, n2 = n2, n1
sr2 = 0
sr1 = 0
for i in range(n - 1, n - n2 - 1, -1):
    sr2 += a[i]
for i in range(n - n2 - 1, n - n1 - n2 - 1, -1):
    sr1 += a[i]
print(sr1 / n1 + sr2 / n2)
