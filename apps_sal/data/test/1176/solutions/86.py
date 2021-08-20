n = int(input())
A = list(map(int, input().split()))
cnt = 0
s = 0
m = 10 ** 9
for ai in A:
    if ai <= 0:
        cnt = cnt + 1
        ai *= -1
    s += ai
    if m > ai:
        m = ai
if cnt % 2 == 0:
    for a in A:
        ans = s
else:
    ans = s - 2 * m
print(ans)
