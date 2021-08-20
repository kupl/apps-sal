(n, k, q) = map(int, input().split())
c = [0] * 200003
for i in range(n):
    (a, b) = map(int, input().split())
    c[a] += 1
    c[b + 1] -= 1
for i in range(1, len(c)):
    c[i] += c[i - 1]
c[0] = 1 if c[0] >= k else 0
for i in range(1, len(c)):
    c[i] = 1 if c[i] >= k else 0
    c[i] += c[i - 1]
ans = ''
for i in range(q):
    (a, b) = map(int, input().split())
    ans += str(c[b] - c[a - 1]) + '\n'
print(ans, end='')
