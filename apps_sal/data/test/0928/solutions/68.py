(n, k) = map(int, input().split())
l = list(map(int, input().split()))
for i in range(1, n):
    l[i] += l[i - 1]
i = 0
j = 0
ans = 0
while j < n:
    if i == 0:
        if k <= l[j]:
            ans += n - j
            i += 1
        else:
            j += 1
    elif k <= l[j] - l[i - 1]:
        ans += n - j
        i += 1
    else:
        j += 1
print(ans)
