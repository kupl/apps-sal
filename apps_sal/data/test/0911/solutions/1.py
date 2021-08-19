(n, c) = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
s1 = s2 = 0
t1 = t2 = 0
for i in range(n):
    t1 += t[i]
    s1 += max(0, p[i] - c * t1)
for i in range(n - 1, -1, -1):
    t2 += t[i]
    s2 += max(0, p[i] - c * t2)
if s1 > s2:
    print('Limak')
elif s2 > s1:
    print('Radewoosh')
else:
    print('Tie')
