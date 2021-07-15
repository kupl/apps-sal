n, k = list(map(int, input().split()))
s = input()
a = set()
k -= 1
q = [s]
i = 0
ans = 0
while i < len(q) and k > 0:
    for j in range(len(q[i])):
        new = q[i][:j] + q[i][j + 1:]
        if new not in a:
            a.add(new)
            q.append(new)
            ans += n - len(q[i]) + 1
            k -= 1
            if k == 0:
                print(ans)
                return
    i += 1
if k == 0:
    print(ans)
else:
    print(-1)

