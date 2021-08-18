import sys
n = int(input())

s = input()
t = input()

ssum = 0
tsum = 0
for i in range(n):
    ssum += int(s[i])
    tsum += int(t[i])

if ssum != tsum:
    print(-1)
    return

nex = [0, 0]

for i in range(n):

    if s[i] == "0" and t[i] == "1":

        if nex[1] > 0:
            nex[1] -= 1
            nex[0] += 1
        else:
            nex[0] += 1

    if s[i] == "1" and t[i] == "0":

        if nex[0] > 0:
            nex[0] -= 1
            nex[1] += 1
        else:
            nex[1] += 1

print(sum(nex))
