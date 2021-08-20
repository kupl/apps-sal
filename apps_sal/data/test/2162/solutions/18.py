from sys import stdin
input = stdin.readline
r = list(map(int, input().split()))
n = sum(r)
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
mp = [0] * -~n
for i in a:
    mp[i] = 0
for i in b:
    mp[i] = 1
for i in c:
    mp[i] = 2
ans = sum(r[:2])
now = ans
sm0 = 0
sm2 = r[2]
for i in range(1, n + 1):
    sm0 += mp[i] == 0
    sm2 -= mp[i] == 2
    if mp[i] == 2:
        now += 1
    elif mp[i] == 1:
        now -= 1
    else:
        now = min(now, n - sm0 - sm2)
    ans = min(ans, now)
print(ans)
