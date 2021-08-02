n, m = list(map(int, input().strip().split()))

s = list(input().strip())

for _ in range(m):
    l, r, c1, c2 = list(input().strip().split())
    for k in range(int(l) - 1, int(r)):
        if s[k] == c1:
            s[k] = c2

print(''.join(s))
