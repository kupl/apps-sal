n = int(input())
m = list(map(int, input().split()))

c = 0

for i in m:
    if i % 2:
        c += 1

uc = n - c

if c <= uc:
    print(c)
    return

b = (c - uc) // 3
c -= b * 3


print(b + min(uc, c))
