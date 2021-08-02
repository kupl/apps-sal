n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mn = [a[i] * (i + 1) * (n - i) for i in range(n)]
mn.sort()
b.sort()
b.reverse()
wyn = 0
for i in range(n):
    wyn = (wyn + b[i] * mn[i]) % 998244353
print(wyn)
