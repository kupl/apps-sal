n = int(input())
sp = list(map(int, input().split()))
k = 10 ** 9 + 1
zn1 = sp[0]
zn2 = sp[-1]

ch2 = min(sp[0], zn2) // (n - 1)
if ch2 < k:
    k = ch2

for i in range(1, n - 1):
    ch1 = min(sp[i], zn1) // i
    ch2 = min(sp[i], zn2) // (n - i - 1)
    if ch2 < k:
        k = ch2
    if ch1 < k:
        k = ch1

ch1 = min(sp[-1], zn1) // (n - 1)
if ch1 < k:
    k = ch1
print(k)
