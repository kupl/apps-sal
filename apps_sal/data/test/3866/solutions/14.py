n = int(input())
if n % 2 == 0:
    print(-1)
    return
print(*list(range(n)))
print(*list(range(n)))
res = []
for i in range(n):
    res += [(2*i) % n]
print(*res)

