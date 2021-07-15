n, v = map(int, input().split())
b = 0
ans = 0
sss = 0
for i in range(1, n + 1):
    while b < v:
        if sss == n - 1:
            break
        sss += 1
        ans += i
        b += 1
    b -= 1
print(ans)
