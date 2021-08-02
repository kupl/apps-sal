n = int(input())
a = list(map(int, input().split()))

a.sort()
minus = n
for i in range(n):
    if a[i] >= 0:
        minus = i
        break

a = list(map(abs, a))
a.sort()

if minus % 2 == 0:
    print((sum(a)))
else:
    print((sum(a) - 2 * a[0]))
