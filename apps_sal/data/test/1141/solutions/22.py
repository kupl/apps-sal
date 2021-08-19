(n, m) = list(map(int, input().split()))
s = list(input())
for _ in range(m):
    (l, r, c1, c2) = input().split()
    for i in range(int(l) - 1, int(r)):
        if s[i] == c1:
            s[i] = c2
print(''.join(s))
