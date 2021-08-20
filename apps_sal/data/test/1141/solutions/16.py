(n, m) = map(int, input().split())
s = list(input())
for i in range(m):
    (l, r, c1, c2) = input().split()
    for j in range(int(l) - 1, int(r)):
        if s[j] == c1:
            s[j] = c2
print(''.join(s))
