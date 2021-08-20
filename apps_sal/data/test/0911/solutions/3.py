(n, c) = map(int, input().split())
(p, t) = (list(map(int, input().split())), list(map(int, input().split())))
(t1, t2, p1, p2) = (0, 0, 0, 0)
for i in range(n):
    t1 += t[i]
    p1 += max(0, p[i] - c * t1)
    t2 += t[n - i - 1]
    p2 += max(0, p[n - i - 1] - c * t2)
if p1 == p2:
    print('Tie')
else:
    print('Limak' if p1 > p2 else 'Radewoosh')
