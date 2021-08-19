(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
tmp = a[0]
i = 0
j = 0
an = 0
for s in a:
    i += 1
    if i < k + 1:
        an += s
    else:
        ans += an
        j += 1
        an -= tmp
        an += s
        tmp = a[j]
ans += an
print(ans / (n - k + 1))
