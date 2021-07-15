n = (int(input()) + 1) // 2
t, p = input().split(), {}
for i in t:
    p[i] = p.get(i, 0) + 1
print('YNEOS'[max(p.values()) > n:: 2])

