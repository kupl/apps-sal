n = int(input())
a = [2, 3, 5, 7]
ans = n
for i in a:
    ans -= n // i
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        ans += n // (a[i] * a[j])
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            ans -= n // (a[i] * a[j] * a[k])
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            for l in range(k + 1, len(a)):
                ans += n // (a[i] * a[j] * a[k] * a[l])
print(ans)
