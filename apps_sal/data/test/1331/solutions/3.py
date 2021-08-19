(n, m, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
ans = 0
z = 0
j = 0
for i in range(len(a)):
    if a[i] == 0:
        z -= 1
        continue
    while j < len(a) and a[j] - a[i] < m:
        if a[j] == 0:
            z += 1
        j += 1
    if j - i - z >= k:
        const = j - i - k - z + 1
        c = 0
        ct = 0
        while ct < const:
            if a[j - 1 - c] != 0:
                a[j - 1 - c] = 0
                ans += 1
                ct += 1
                if j - 1 - c != i:
                    z += 1
            c += 1
print(ans)
