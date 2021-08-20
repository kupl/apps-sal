n = int(input())
l = list(map(int, input().split()))
l.sort()
maksik = -10000000
for i in range(n):
    if l[i] == 1 and maksik < 1:
        maksik = 1
        continue
    elif l[i] - 1 > maksik:
        l[i] -= 1
        maksik = l[i]
    elif l[i] - 1 == maksik:
        maksik = l[i]
    else:
        l[i] += 1
        maksik = l[i]
wyn = 0
for i in range(1, n):
    if l[i] != l[i - 1]:
        wyn += 1
print(wyn + 1)
