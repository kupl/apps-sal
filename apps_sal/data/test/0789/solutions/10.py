a = list(str(input()))
a = [int(x) for x in a]
n = len(a)
ans = 0
for i in range(n):
    digs = n - i
    ans += 2 ** (digs - 1)
    if a[i] == 4:
        continue
    else:
        ans += 2 ** (digs - 1)
print(ans)
