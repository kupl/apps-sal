s = input()
s = [int(i) for i in s]
s.reverse()
ans = [0] * len(s)
f = 0
(r0, r1) = (0, 0)
for i in s:
    if i == 2:
        while r0:
            r0 -= 1
            ans[f] = 0
            f += 1
        ans[f] = 2
        f += 1
    elif i == 1:
        r1 += 1
    else:
        r0 += 1
while r1:
    r1 -= 1
    ans[f] = 1
    f += 1
while r0:
    r0 -= 1
    ans[f] = 0
    f += 1
ans.reverse()
for i in ans:
    print(i, end='')
