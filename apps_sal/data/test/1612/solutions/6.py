n = int(input())
t, l, s = [0] * n, [0] * n, ['YES'] * n
for i in range(n):
    p = tuple(map(int, input().split()))
    t[i], l[i] = set(p[1: ]), p[0]
for i in range(n):
    for j in range(i + 1, n):
        if l[i] < l[j]:
            if all(k in t[j] for k in t[i]): s[j] = 'NO'
        else:
            if all(k in t[i] for k in t[j]): 
                if l[i] == l[j]: s[j] = 'NO'
                s[i] = 'NO'
print('\n'.join(s))
