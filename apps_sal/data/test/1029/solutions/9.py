p = input().strip()

n = len(p)
j = n - 1
ans = 0

while(j >= 0):
    k = j
    while p[k] == '0':
        k -= 1

    ln = j - k + 1

    if ln > k:
        ans += 1
        j = -1

    elif ln == k:
        if (p[0] >= p[k]):
            j = k - 1
        else:
            j = -1
        ans += 1

    else:
        ans += 1
        j = k - 1

print(ans)
