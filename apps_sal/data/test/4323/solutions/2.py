n, m = [int(i) for i in input().split()]
diff = []
s = 0
for i in range(n):
    a, b = [int(j) for j in input().split()]
    diff.append(a - b)
    s += a
diff.sort()
ans = 0
for i in reversed(range(n)):
    if s <= m:
        break
    s -= diff[i]
    ans += 1
if s <= m:
    print(ans)
else:
    print(-1)
