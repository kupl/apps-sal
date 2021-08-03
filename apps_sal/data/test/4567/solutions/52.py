N = int(input())
s = [int(input()) for _ in range(N)]
mn = 101
for n in range(N):
    if s[n] % 10 != 0:
        mn = min(mn, s[n])
if mn == 101:
    print((0))
else:
    ss = sum(s)
    print((ss if ss % 10 != 0 else ss - mn))
