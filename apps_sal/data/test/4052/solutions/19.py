n = int(input())
s = input()
t = input()
res = []
count = 0
for i in range(n):
    if t[i] not in s:
        print(-1)
        return
    else:
        ind = s.index(t[i])
        for j in range(ind, 0, -1):
            res.append(count + j)
        s = s[:ind] + s[ind + 1:]
        count += 1

k = len(res)
if k > 10**4:
    print(-1)
else:
    print(k)
    print(*res)
