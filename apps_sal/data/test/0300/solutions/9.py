n = int(input())
a = list(map(int, input().split()))
a.sort()
total = sum(a)
need = 4.5 * n
i = 0
while total < need:
    total += (5 - a[i])
    i += 1
print(i)
