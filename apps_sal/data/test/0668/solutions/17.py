n = int(input())
a = list(enumerate(list(map(int, input().split())), start=1))
a = [a[0]] + sorted(a[1:], key=lambda x: x[1], reverse=True)

used = [0] * n
used[0] = 1
ans = [list() for i in range(n)]
total = 0
for i in range(n):
    if not(0 in used):
        break
    else:
        cnt = 0
        j = i + 1
        if j != n:
            while j < n and cnt < a[i][1]:
                if not used[j]:
                    used[j] = 1
                    total += 1
                    ans[i].append(a[j])
                    cnt += 1
                j += 1
if 0 in used:
    print(-1)
else:
    print(total)
    for i in range(n):
        for j in range(len(ans[i])):
            print(a[i][0], ans[i][j][0])
