n = int(input())
a = list(map(int, input().split()))
c = 1
v = 0
p = a[0]

for i in range(1, n):
    if a[i] == a[i - 1]:
        c += 1
    else:
        while c > 0 and p < a[i]:
            v += (c % 2)
            c //= 2
            p += 1
        c += 1
        p = a[i]

while c > 1:
    v += (c % 2)
    c //= 2
    p += 1

print(p - v)
