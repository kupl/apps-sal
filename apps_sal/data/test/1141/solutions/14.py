(n, m) = map(int, input().split())
s = list(input())
for _ in range(m):
    (l, r, a, b) = input().split()
    (l, r) = map(int, (l, r))
    for i in range(l - 1, r):
        if s[i] == a:
            s[i] = b
print(''.join(s))
