n, m = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
value = [0] * (m + 1)
length = [0] * (m + 1)
ans = 0
for i in range(1, n):
    a, b = A[i - 1], A[i]
    if a < b:
        value[a + 1] += 1
        value[b + 1] -= 1
        length[b + 1] -= (b - a)
        ans += b - a
    else:
        value[a + 1] += 1
        value[m] -= 1
        value[0] += 1
        value[b + 1] -= 1
        length[0] += (m - a - 1)
        length[b + 1] -= (m - a) + (b)
        ans += m - a + b
for i in range(m):
    value[i + 1] = value[i] + value[i + 1]
for i in range(m + 1):
    length[i] += value[i]
for i in range(m):
    length[i + 1] += length[i]
for i in range(m):
    length[i] -= value[i]
ans -= max(length[::-1])
print(ans)
