t = int(input())
all = []
for i in range(1, 10):
    for j in range(1, 10):
        all.append(int(str(i) * j))
for i in range(t):
    n = int(input())
    ans = 0
    for i in range(len(all)):
        if all[i] <= n:
            ans += 1
    print(ans)
