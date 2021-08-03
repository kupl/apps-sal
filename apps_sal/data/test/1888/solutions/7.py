n, m = (map(int, input().split()))
s = [0] * n
for i in range(m):
    a, b, c = (map(int, input().split()))
    s[a - 1] -= c
    s[b - 1] += c
print(sum(s[i] for i in range(n) if s[i] > 0))
