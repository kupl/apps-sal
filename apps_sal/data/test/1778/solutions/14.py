n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0 for i in range(n)]
a += c
b += c
sa = 0
sb = 0
a.sort(reverse=True)
b.sort(reverse=True)
d = 0
i = 0
j = 0
for p in range(2 * n):
    if p % 2 == 0:
        if a[i] > b[j]:
            sa += a[i]
            i += 1
        else:
            j += 1
    elif p % 2 == 1:
        if b[j] > a[i]:
            sb += b[j]
            j += 1
        else:
            i += 1
print(sa - sb)
