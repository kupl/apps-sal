import sys
if False:
    inp = open('A.txt', 'r')
else:
    inp = sys.stdin
(n, s) = list(map(int, inp.readline().split()))
ans = s
for i in range(n):
    (floor, time) = list(map(int, inp.readline().split()))
    if s - floor < time:
        ans = max(ans, time + floor)
    else:
        pass
print(ans)
