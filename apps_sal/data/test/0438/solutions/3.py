n = int(input())
ans = 0
L = []
i = 1
while i <= n:
    ans += 1
    L.append(i)
    n -= i
    i += 1
L[-1] += n
print(ans)
print(*L)
