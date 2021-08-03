n = int(input())
a = list(map(int, input().split()))

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

t = 0
ans = []
for k, v in sorted(d.items(), key=lambda x: x[0], reverse=True):
    if v >= 4 and t == 0:
        print(k * k)
        return
    elif v >= 2:
        ans.append(k)
        t += 1
    if t == 2:
        print(ans[0] * ans[1])
        return
print(0)
