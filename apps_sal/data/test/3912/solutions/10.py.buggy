mp, a, p = {}, [], []
n = int(input())
for i in input():
    if i in mp:
        mp[i] += 1
    else:
        mp[i] = 1
odd = 0
for i in mp:
    if mp[i] & 1:
        a.append(i)
        mp[i] -= 1
        odd += 1
    if mp[i]:
        p.append(i)
m = max(1, odd)
for i in range(m, n + 1):
    if not n % i:
        d = n // i
        if odd and not d & 1:
            continue
        print(i)
        for K in range(i - m):
            a.append(p[-1])
            if mp[p[-1]] > 1:
                mp[p[-1]] -= 1
            else:
                p.pop()
        for k in range(i):
            s = ''
            for j in range(d // 2):
                s += p[-1]
                mp[p[-1]] -= 2
                if not mp[p[-1]]:
                    p.pop()
            if odd:
                print(s + a.pop() + s[::-1], end=' ')
            else:
                print(s + s[::-1], end=' ')
        return
