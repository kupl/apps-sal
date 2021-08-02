k = int(input())

t = ["" for i in range(4)]
for i in range(4):
    t[i] = input()

cnt = [0 for i in range(10)]

for i in range(4):
    for j in range(4):
        if t[i][j] != '.':
            cnt[int(t[i][j])] += 1

if max(cnt) <= k * 2:
    print("YES")
else:
    print("NO")
