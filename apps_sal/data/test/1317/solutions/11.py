s = input().split()
n = int(s[0])
m = int(s[1])
ans = 0
for i in range(1, min(n + 1, m + 1)):
    ii = i ** 2
    for j in range(i, min(n + 1, m + 1)):
        jj = j ** 2
        if (ii + jj) % m == 0:
            if j > i:
                ans += (1 + (n - j) // m) * (1 + (n - i) // m) * 2
            else:
                ans += (1 + (n - j) // m) ** 2
print(ans)
