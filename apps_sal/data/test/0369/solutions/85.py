from bisect import *
n, m = list(map(int, input().split()))
s = input()

masu = []
for i in range(n + 1):
    if s[i] == "0":
        masu.append(i)

now = n
ans = [n]

while now > 0:
    next = masu[bisect_left(masu, now - m)]
    if now != next:
        ans.append(next)
        now = next
    else:
        ans = -1
        break

if ans == -1:
    print((-1))

else:
    ans.reverse()
    for i in range(len(ans) - 1):
        print((ans[i + 1] - ans[i]))
