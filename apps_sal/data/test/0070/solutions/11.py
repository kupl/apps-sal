n, k = input().split()
k = int(k)

ans = 0
nz = 0
for c in reversed(n):
    if nz == k:
        break
    if c == '0':
        nz += 1
    else:
        ans += 1
else:
    ans = len(n) - 1

print(ans)

