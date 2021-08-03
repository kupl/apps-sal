n = int(input())
a = [int(t) for t in input().split(' ')]

INF = 10**10

i = n - 1
total = 0
mn = INF
while i >= 0:
    mn = max(0, min(mn - 1, a[i]))
    total += mn
    i -= 1

print(total)
