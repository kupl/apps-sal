t = int(input())
buf = []
for _ in range(t):
    a, k = input().split()
    k = int(k) - 1
    for _ in range(k):
        c = min(a)
        d = max(a)
        a = str(int(a) + int(c) * int(d))
        if '0' in a:
            break
    buf.append(a)

print('\n'.join(buf))

