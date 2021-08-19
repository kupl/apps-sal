(n, m) = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
b.append(-1)
f = 0
ans = 0
for i in a:
    if b[f] >= i:
        f += 1
        ans += 1
print(ans)
