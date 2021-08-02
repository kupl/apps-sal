n = int(input())
d = list(map(int, input().split()))
calls = dict()
invalid = False
c = 0
for i in range(n):
    if d[i] > 0:
        if d[i] in calls.keys(): calls[d[i]] += 1
        else: calls[d[i]] = 1
        if calls[d[i]] == 2:
            c += 1
        elif calls[d[i]] == 3:
            invalid = True
            break

if invalid: print(-1)
else: print(c)
