from fractions import gcd
n = int(input())
a = list(map(int, input().split()))
prev = a[0]
k = 0
for c in a[1:]:
    if gcd(prev, c) != 1:
        k += 1
    prev = c
print(k)
prev = a[0]
for c in a[1:]:
    print(prev, end=' ')
    if gcd(prev, c) != 1:
        print(1, end=' ')
    prev = c
print(prev)
