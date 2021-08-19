(h, w) = list(map(int, input().split()))
ans = set()
good = True
for i in range(h):
    s = input()
    pg = -1
    ps = -1
    for j in range(w):
        if s[j] == 'G':
            pg = j
        elif s[j] == 'S':
            ps = j
    if ps < pg:
        good = False
    ans.add(ps - pg)
if not good:
    print(-1)
else:
    print(len(ans))
