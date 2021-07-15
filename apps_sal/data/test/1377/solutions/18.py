n = int(input())
data = [int(i) for i in input().split()]
ind = [0] * (n+1)
for i in range(n):
    ind[data[i]] = i
li = ind[n] - 1
ri = ind[n] + 1
good = True
for i in range(n - 1, 0, -1):
    if ind[i] == ri:
        ri += 1
        continue
    if ind[i] == li:
        li -= 1
        continue
    good = False
    break
if good:
    print("YES")
else:
    print("NO")
