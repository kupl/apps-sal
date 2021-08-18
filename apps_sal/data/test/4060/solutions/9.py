n = int(input())
s = input()
ans = 0
s1, s2 = [], []
f1 = [1] * n
f2 = [1] * n
for i in range(n):
    s1.append([0, 0])
    s2.append([0, 0])
if s[0] == '(':
    s1[0][0] += 1
else:
    s1[0][1] += 1
for i in range(1, n):
    s1[i][0] = s1[i - 1][0]
    s1[i][1] = s1[i - 1][1]
    if s[i] == '(':
        s1[i][0] += 1
    else:
        s1[i][1] += 1
if s[-1] == '(':
    s2[-1][0] += 1
else:
    s2[-1][1] += 1
for i in range(n - 2, -1, -1):
    s2[i][0] = s2[i + 1][0]
    s2[i][1] = s2[i + 1][1]
    if s[i] == '(':
        s2[i][0] += 1
    else:
        s2[i][1] += 1
if s[0] == ')':
    f1[0] = 0
for i in range(1, n):
    if f1[i - 1] == 1 and s1[i][1] <= s1[i][0]:
        f1[i] = 1
    else:
        f1[i] = 0
if s[-1] == '(':
    f2[-1] = 0
for i in range(n - 2, -1, -1):
    if f2[i + 1] == 1 and s2[i][0] <= s2[i][1]:
        f2[i] = 1
    else:
        f2[i] = 0
for i in range(n):
    t1 = s1[-1][0]
    t2 = s1[-1][1]
    if i % 2 == 1:
        if i + 1 < n:
            p1 = s2[i + 1][0]
            p2 = s2[i + 1][1]
            if p1 > p2 or f2[i + 1] == 0:
                continue
        p1 = s1[i][0]
        p2 = s1[i][1]
        q1 = s2[i][0]
        q2 = s2[i][1]
        if s[i] == '(':
            p1 -= 1
            p2 += 1
            t1 -= 1
            t2 += 1
            q1 -= 1
            q2 += 1
        else:
            p2 -= 1
            p1 += 1
            t1 += 1
            t2 -= 1
            q2 -= 1
            q1 += 1
        if p2 > p1:
            continue
        if q1 > q2:
            continue
        if i - 1 >= 0 and f1[i - 1] == 0:
            continue
        if t1 == t2:
            ans += 1
    else:
        if i - 1 >= 0:
            p1 = s1[i - 1][0]
            p2 = s1[i - 1][1]
            if p2 > p1 or f1[i - 1] == 0:
                continue
        p1 = s2[i][0]
        p2 = s2[i][1]
        q1 = s1[i][0]
        q2 = s1[i][1]
        if s[i] == '(':
            p1 -= 1
            p2 += 1
            t1 -= 1
            t2 += 1
            q1 -= 1
            q2 += 1
        else:
            p1 += 1
            p2 -= 1
            t1 += 1
            t2 -= 1
            q1 += 1
            q2 -= 1
        if p2 < p1:
            continue
        if q1 < q2:
            continue
        if i + 1 < n and f2[i + 1] == 0:
            continue
        if t1 == t2:
            ans += 1
print(ans)
