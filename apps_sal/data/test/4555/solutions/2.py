a, b, k = map(int, input().split())

ans = set()
r = range(a, b + 1)
for i in range(min(k, len(r))):
    ans.add(r[i])
    ans.add(r[-i-1])
else:
    [print(i) for i in sorted(ans)]
