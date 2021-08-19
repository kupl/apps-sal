
def mi():
    return map(int, input().split())


n = int(input())
a = list(mi())
b = list(mi())

a.sort(reverse=True)
b.sort(reverse=True)

i, j = 0, 0
sa, sb = 0, 0
for k in range(2 * n):
    if k & 1:
        if j == n:
            a[i] = 0
            i += 1
            continue
        if i == n:
            sb += b[j]
            j += 1
            continue
        if b[j] < a[i]:
            a[i] = 0
            i += 1
        else:
            sb += b[j]
            b[j] = 0
            j += 1

    else:
        if i == n:
            b[j] = 0
            j += 1
            continue
        if j == n:
            sa += a[i]
            i += 1
            continue
        if a[i] < b[j]:
            b[j] = 0
            j += 1
        else:
            sa += a[i]
            a[i] = 0
            i += 1
# sa+=sum(a)
# sb+=sum(b)
print(sa - sb)
