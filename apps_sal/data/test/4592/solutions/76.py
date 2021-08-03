n = int(input())
l = {}
ans = 1

for i in range(2, n + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            cnt = 0
            while i % j == 0:
                i //= j
                cnt += 1
            if j in l:
                v = l[j]
                l[j] = cnt + v
            else:
                l[j] = cnt
for i in l.values():
    ans = ans * (i + 1) % (10**9 + 7)

print(ans)
