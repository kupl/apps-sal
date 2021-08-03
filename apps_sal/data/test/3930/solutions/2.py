n, k = [int(x) for x in input().split()]
acc = 0
ans = 0
prefix = {0: 1}
for a in input().split():
    acc += int(a)
    ans += prefix.get(acc - 1, 0)
    i = k
    while i != 1 and i <= 10**14 and i >= -(10**14):
        ans += prefix.get(acc - i, 0)
        i *= k
    prefix.setdefault(acc, 0)
    prefix[acc] += 1
print(ans)
