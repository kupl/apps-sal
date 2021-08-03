n, m = list(map(int, input().split()))

s = [c for c in input()]

for _ in range(m):
    l, r, a, b = input().split()
    l = int(l) - 1
    r = int(r)

    for i in range(l, r):
        if s[i] == a:
            s[i] = b
print(''.join(s))
