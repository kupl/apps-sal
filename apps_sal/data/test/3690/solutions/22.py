h, m, s, t1, t2 = map(int, input().split())
ls = s * 2
lm = m * 2
if ls != 0:
    lm += 1
lh = h % 12 * 10
if ls != 0 or lm != 0:
    lh += 1
t1 = t1 % 12 * 10
t2 = t2 % 12 * 10
t1, t2 = min(t1, t2), max(t1, t2)
ans = False
ans1 = True
ans2 = True
if t1 <= ls <= t2 or t1 <= lm <= t2 or t1 <= lh <= t2:
    ans1 = False
#print(ans1)
if 0 <= ls <= t1 or 0 <= lm <= t1 or 0 <= lh <= t1:
    ans2 = False
#print(ans2)
if t2 <= ls <= 118 or t2 <= lm <= 118 or t2 <= lh <= 118:
    ans2 = False
#print(ans2)
if ans1 or ans2:
    ans = True
if ans:
    print('YES')
else:
    print('NO')
