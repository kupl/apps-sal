N = int(input())
A = list(map(int, input().split()))
zflag = False
ans = 0
cnt = 1

for a in A:
    if a == 0:
        zflag = True
        ans += 1
    elif a < 0:
        cnt *= -1
        ans += abs(-1 - a)
    else:
        ans += abs(1 - a)

if not zflag and cnt == -1:
    ans += 2

print(ans)
