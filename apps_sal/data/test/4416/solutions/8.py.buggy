import sys
input = sys.stdin.readline
n, minn = map(int, input().split())
a = []
ca, cb = 0, 0
for i in range(n):
    t, x, y = map(int, input().split())
    if x == 1:
        ca += 1
    if y == 1:
        cb += 1
    a.append((t, x, y))
if ca < minn or cb < minn:
    print(-1)
    return
ca, cb = 0, 0
alice = []
bob = []
both = []
for i in range(n):
    if a[i][1] == a[i][2] == 1:
        both.append(a[i][0])
    elif a[i][1] != a[i][2]:
        if a[i][1] == 1:
            alice.append(a[i][0])
        else:
            bob.append(a[i][0])
alice.sort()
bob.sort()
both.sort()
# print (alice)
# print (bob)
# print (both)
i, j, k = 0, 0, 0
ans = 0
while ca < minn or cb < minn:
    if (i < len(alice) and j < len(bob) and k < len(both)) and alice[i] + bob[j] <= both[k]:
        ans += alice[i] + bob[j]
        ca += 1
        cb += 1
        i += 1
        j += 1
    elif (i < len(alice) and j < len(bob) and k < len(both)) and alice[i] + bob[j] >= both[k]:
        ans += both[k]
        ca += 1
        cb += 1
        k += 1
    else:
        break

if i == len(alice):
    while ca < minn:
        ans += both[k]
        k += 1
        ca += 1
        cb += 1
if j == len(bob):
    while cb < minn:
        ans += both[k]
        k += 1
        ca += 1
        cb += 1
if k == len(both):
    while ca < minn:
        ans += alice[i]
        i += 1
        ca += 1
    while cb < minn:
        ans += bob[j]
        j += 1
        cb += 1
print(ans)
