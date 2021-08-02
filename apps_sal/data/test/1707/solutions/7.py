n = int(input())
l = list(map(int, input().split()))
a = [abs(l[i]) for i in range(n)]
a.sort()
wyn = 0
wsk1 = 0
wsk2 = 1
licz = 0
while True:
    if a[wsk1] * 2 < a[wsk2]:
        wyn += (wsk2 - wsk1 - 1)
        wsk1 += 1
    else:
        wsk2 += 1
    if wsk2 == n:
        break
wyn += (n - wsk1) * (n - wsk1 - 1) // 2
print(wyn)
