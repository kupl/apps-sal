(n, r) = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]
b = [0] * n
ans = 0
for i in range(n):
    if b[i] == 0:
        found = False
        for j in range(min(n - 1, i + r - 1), max(-1, i - r), -1):
            if a[j] == 1:
                for k in range(min(n - 1, j + r - 1), max(-1, j - r), -1):
                    b[k] = 1
                ans += 1
                found = True
                break
        if not found:
            ans = -1
            break
print(ans)
