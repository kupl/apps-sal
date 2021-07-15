N = int(input())
L = {}
R = {}
Z = 0
ans = 0
for i in range(N):
    s = input()
    ok = 1
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1
        else:
            if cnt == 0:
                ok = 0
                break
            cnt -= 1
    if ok:
        if cnt == 0:
            if Z == 1:
                ans += 1
            Z ^= 1
        else:
            if R.get(cnt, 0) > 0:
                ans += 1
                R[cnt] -= 1
            else:
                L[cnt] = L.get(cnt, 0) + 1
        continue

    ok = 1
    for c in reversed(s):
        if c == ')':
            cnt += 1
        else:
            if cnt == 0:
                ok = 0
                break
            cnt -= 1
    if ok:
        if cnt == 0:
            if Z == 1:
                ans += 1
            Z ^= 1
        else:
            if L.get(cnt, 0) > 0:
                ans += 1
                L[cnt] -= 1
            else:
                R[cnt] = R.get(cnt, 0) + 1
print(ans)
