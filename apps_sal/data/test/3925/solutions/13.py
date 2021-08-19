from collections import deque
s2 = deque(input())
s4 = s2.copy()
s1 = deque()
s1.append(s2[0])
s2.popleft()
t = True
while len(s2) > 0:
    if t:
        if s1[-1] != s2[0]:
            s1.append(s2[0])
            s2.popleft()
        elif s1[0] != s2[-1]:
            t = False
        else:
            s1 += s2
            break
    elif s1[0] != s2[-1]:
        s1.appendleft(s2[-1])
        s2.pop()
    elif s1[-1] != s2[0]:
        t = True
    else:
        s1 += s2
        break
ans = 1
x = 1
for i in range(1, len(s1)):
    if s1[i] != s1[i - 1]:
        x += 1
    else:
        ans = max(ans, x)
        x = 1
ans = max(ans, x)
s2 = s4.copy()
s2.reverse()
s1 = deque()
s1.append(s2[0])
s2.popleft()
t = True
while len(s2) > 0:
    if t:
        if s1[-1] != s2[0]:
            s1.append(s2[0])
            s2.popleft()
        elif s1[0] != s2[-1]:
            t = False
        else:
            s1 += s2
            break
    elif s1[0] != s2[-1]:
        s1.appendleft(s2[-1])
        s2.pop()
    elif s1[-1] != s2[0]:
        t = True
    else:
        s1 += s2
        break
ans1 = 1
x = 1
for i in range(1, len(s1)):
    if s1[i] != s1[i - 1]:
        x += 1
    else:
        ans1 = max(ans1, x)
        x = 1
ans1 = max(ans1, x)
print(max(ans1, ans))
