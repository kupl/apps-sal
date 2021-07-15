n, k = map(int, input().split())
s = []
for i in range(n):
    l, r = map(int, input().split())
    s.append([r, l, i]) # Greedy on largest right endpoint
s.sort()

ans = []
for i in range(201):
    a = 0
    u = []
    for tmp in s:
        if i <= tmp[0] and i >= tmp[1]:
            a += 1
            if a > k:
                u.append(tmp)
                ans.append(tmp[2] + 1)
    for tmp in u:
        s.remove(tmp)
print(len(ans))
print(' '.join(map(str, ans)))
