# Author:      Divesh Uttamchandani
# Institution: BITS Pilani
n = int(input().strip())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
pos_of = [-1 for i in range(2 * 10**5 + 1)]

for i, ele in enumerate(a):
    pos_of[ele] = i + 1

current_pos = 0
ans = []
for i in b:
    if(pos_of[i] > current_pos):
        ans.append(pos_of[i] - current_pos)
        current_pos = pos_of[i]
    else:
        ans.append(0)

print(' '.join(list(map(str, ans))))
# <> with <3 using Termicoder:
# https://termicoder.github.io
