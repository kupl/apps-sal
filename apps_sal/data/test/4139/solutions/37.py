N = int(input())
T = ['3', '5', '7']
l = T.copy()
ans = 0
while l:
    n = l.pop()
    if int(n) > N:
        continue
    if len(set(n)) == 3:
        ans += 1
    for t in T:
        l.append(n + t)
print(ans)
