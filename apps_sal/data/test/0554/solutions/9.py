n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
total = 0
for i in range(m):
    l, r = list(map(int, input().split()))
    ai = a[l - 1:r]
    sumai = sum(ai)
    if (sumai > 0):
        total += sumai

print(total)
