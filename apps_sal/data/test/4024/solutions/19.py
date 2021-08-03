# your code goes here
n, k = map(int, input().split())
s = input()
c = 0
q = [s]
d = set()
ls = 0
while q:
    p = q.pop(0)
    if p not in d:
        ls += 1
        c += (n - len(p))
        if ls == k:
            break
        d.add(p)
        for i in range(len(p)):
            temp = p[:i] + p[i + 1:]
            if temp not in d:
                q.append(temp)

if ls == k:
    print(c)
else:
    print(-1)
