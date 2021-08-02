def r():
    return list(map(int, input().split()))


n = int(input())
a = r()
for i in range((n + 1) // 2):
    if i & 1:
        continue
    tmp = a[i]
    a[i] = a[n - i - 1]
    a[n - i - 1] = tmp
print(' '.join(str(i) for i in a))
