from sys import stderr
N = int(input())
data = [int(i) for i in input().split()]
data.append(0)
data.append(0)
data.append(0)

ans = 0
ins = 0
last = -1
for i in range(N):
    if data[i] == 1:
        last = i

if last == -1:
    print(0)
    return

for i in range(last + 1):
    if data[i] == 1 and ins == 0:
        ans += 1
        ins = 1
        continue
    if data[i] == 1 and ins == 1:
        ans += 1
        continue
    if data[i] == 0 and ins == 1:
        ans += 1
        if data[i + 1] == 0:
            ins = 0
        continue

print(ans)
