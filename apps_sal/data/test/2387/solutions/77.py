# F - Bracket Sequencing
import sys
readline = sys.stdin.readline

N = int(input())
L = []
R = []
for _ in range(N):
    S = readline().strip()
    sums = 0
    mins = 0
    for s in S:
        if s == '(':
            sums += 1
        else:
            sums -= 1
            mins = min(mins, sums)
    if sums >= 0:
        L.append((sums, mins))
    else:
        R.append((-sums, mins-sums))

L.sort(key=lambda x: x[1], reverse=True)
R.sort(key=lambda x: x[1], reverse=True)

ans = 'Yes'
l_now = 0
for d, min_d in L:
    if l_now + min_d < 0:
        ans = 'No'
        break
    else:
        l_now += d

r_now = 0
for d, min_d in R:
    if r_now + min_d < 0:
        ans = 'No'
        break
    else:
        r_now += d

if l_now != r_now:
    ans = 'No'

print(ans)
