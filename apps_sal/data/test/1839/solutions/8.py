n = int(input())
sa = set()
sb = set()
l = []
for i in range(n * n):
    a, b = list(map(int, input().split()))
    if not(a in sa) and not(b in sb):
        l += [str(i + 1)]
        sa.add(a)
        sb.add(b)
print(' '.join(l))
