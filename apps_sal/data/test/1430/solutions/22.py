import sys

icase = 0
if icase == 0:
    n, k = list(map(int, input().split()))
    s = input()

if n == 1:
    print((1))
    return

ss = []
if s[0] == "1" and s[1] == "1":
    zcnt = 1
elif s[0] == "1" and s[1] == "0":
    #    ss.append(1)
    zcnt = 1
elif s[0] == "0" and s[1] == "0":
    ss.append(0)
    zcnt = 1
elif s[0] == "0" and s[1] == "1":
    ss.append(0)
#    ss.append(1)
    zcnt = 1

for i in range(1, n - 1):
    if s[i] == "0" and s[i - 1] == "0":
        zcnt += 1
    elif s[i] == "0" and s[i - 1] == "1":
        ss.append(zcnt)
        zcnt = 1
    elif s[i] == "1" and s[i - 1] == "1":
        zcnt += 1
    elif s[i] == "1" and s[i - 1] == "0":
        ss.append(zcnt)
        zcnt = 1

for i in range(n - 1, n):
    if s[i] == "0" and s[i - 1] == "0":
        zcnt += 1
        ss.append(zcnt)
        ss.append(0)
    elif s[i] == "0" and s[i - 1] == "1":
        ss.append(zcnt)
        ss.append(1)
        ss.append(0)
    elif s[i] == "1" and s[i - 1] == "1":
        zcnt += 1
        ss.append(zcnt)
    elif s[i] == "1" and s[i - 1] == "0":
        ss.append(zcnt)
        ss.append(1)

# print(ss)

if len(ss) <= 2 * k + 1:
    print(n)
    return

smax = 0
for i in range(2 * k + 1):
    smax += ss[i]
# print(smax)
ssum = smax
kk = 2 * k
for i in range(2, len(ss) - kk, 2):
    ssum = ssum - ss[i - 2] - ss[i - 1] + ss[i + kk - 1] + ss[i + kk]
    smax = max(smax, ssum)

print(smax)
