n, m = map(int, input().split())
a = []
for i in range(1, int(m**.5) + 1):
    if m % i == 0:
        ans = i
        a.append(i)
    if i == m // n:
        break
else:
    for i in a:
        if m // i <= m // n:
            ans = m // i
            break
print(ans)
