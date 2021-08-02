n = int(input())
a = [int(v) for v in input().split()]

bestd = len(a)
mi = 0
m = a[0]
for i in range(1, len(a)):
    if a[i] < m:
        m = a[i]
        mi = i
        bestd = len(a)
    elif a[i] == m:
        currd = i - mi
        if currd < bestd:
            bestd = currd
        mi = i

print(bestd)
