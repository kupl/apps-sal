n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
s = list(map(int, input().split()))
d = [0] * m
f = []
for q in range(len(s)):
    if s[q] == 1:
        f.append(a[q])
q2, q1 = -float('inf'), f[0]
q3, q4 = -1, 0
for q in range(len(a)):
    if s[q] == 1:
        q2, q1 = a[q], f[q4 + 1] if len(f) > q4 + 1 else float('inf')
        q3, q4 = q3 + 1, q4 + 1
    else:
        if q2 == -float('inf'):
            d[q4] += 1
        elif q1 == float('inf'):
            d[q3] += 1
        else:
            if a[q] - q2 <= q1 - a[q]:
                d[q3] += 1
            else:
                d[q4] += 1
print(*d)
