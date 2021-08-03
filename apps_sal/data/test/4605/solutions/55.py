n, a, b = list(map(int, input().split()))

l = list(range(0))

for i in range(n + 1):
    res = sum(list(map(int, str(i))))
    if res >= a and res <= b:
        l.append(i)

ans = sum(list(l))
print(ans)
