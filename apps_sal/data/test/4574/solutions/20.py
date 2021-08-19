n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
b = a.copy()
b = list(set(b))
b.sort(reverse=True)
c = [0] * len(b)
j = 0
c[j] = 1
for i in range(1, n):
    if a[i - 1] == a[i]:
        c[j] += 1
    else:
        j += 1
        c[j] += 1
for i in range(len(b)):
    if c[i] >= 4:
        ans = b[i] * b[i]
        break
    elif c[i] >= 2:
        for j in range(i + 1, len(b)):
            if c[j] >= 2:
                ans = b[i] * b[j]
                break
        break
print(ans)
