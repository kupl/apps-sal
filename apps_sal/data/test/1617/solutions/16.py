n = int(input())
l = []
s = set()
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        s.add(int(i))
        s.add(int(n // i))

ans = []
for x in s:
    k = n // x
    last = 1 + x * (k - 1)
    ans.append((1 + last) * k // 2)
ans = sorted(ans)
for i in ans:
    print(i, end=' ')
