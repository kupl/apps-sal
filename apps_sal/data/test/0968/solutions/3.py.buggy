import sys

n = int(input())

name = []
for i in range(n):
    s = input().split()
    name.append(s)

p = list(map(int, input().split()))
for i in range(n):
    p[i] -= 1

new = [0] * n
for i in range(n):
    new[i] = name[p[i]]


now = min(new[0][0], new[0][1])

for i in range(1, n):
    tmp1 = min(new[i][0], new[i][1])
    tmp2 = max(new[i][0], new[i][1])

    if now < tmp1:
        now = tmp1
    elif now < tmp2:
        now = tmp2
    else:
        print("NO")
        return

print("YES")
