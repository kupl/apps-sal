n, m = input().split()
n = int(n)
m = int(m)
ans = 0
for i in range(31):
    for j in range(20):
        if 2 ** i * 3 ** j >= n and 2 ** i * 3 ** j <= m:
            ans = ans + 1
print(ans)
