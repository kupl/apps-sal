def I():
    return map(int, input().split())


n = int(input())
a = list(I())
a.sort(reverse=True)
(x, f) = I()
summ = 0
for i in range(n):
    if a[i] > x:
        r = (a[i] - x) // (x + f)
        if (a[i] - x) % (x + f):
            r += 1
        summ += f * r
    else:
        break
print(summ)
