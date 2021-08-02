import math

n = int(input())
s = input()

eS = [0] * n
wS = [0] * n

ec = 0
for i in range(n):
    eS[i] = ec
    if s[i] == "W":
        ec += 1

wc = 0
for i in reversed(list(range(n))):
    wS[i] = wc
    if s[i] == "E":
        wc += 1

ans = 10000000

for i in range(n):
    ans = min(ans, eS[i] + wS[i])

print(ans)
