n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))
bar = ['Limak', 'Tie', 'Radewoosh']
s1 = 0
t1 = 0
s2 = 0
t2 = 0
for i in range(n):
    t1 += t[i]
    t2 += t[n - i - 1]
    s1 += max(0, p[i] - t1 * c)
    s2 += max(0, p[n - i - 1] - t2 * c)
if s1 > s2:
    print(bar[0])
elif s1 < s2:
    print(bar[2])
else:
    print(bar[1])
