n, k = list(map(int, input().split()))
s = [int(i) for i in input().split()]
s.sort()
ans = 0
for i in s:
    while k < i / 2:
        ans += 1
        k = 2 * k
    k = max(k, i)
print(ans)
