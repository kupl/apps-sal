def R(): return map(int, input().split())


n = int(input())

a = list(R())

s = 0

for i in range(n):
    if a[i] >= 0:
        s += a[i]
    else:
        s -= a[i]

print(s)
