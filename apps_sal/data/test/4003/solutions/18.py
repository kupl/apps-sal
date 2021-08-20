from collections import deque
n = int(input())
a = deque([int(x) for x in input().split()])
cur = -1
ans = ''
while cur < a[0] or cur < a[-1]:
    if a[0] < a[-1]:
        if cur < a[0]:
            ans += 'L'
            cur = a[0]
            a.popleft()
        else:
            ans += 'R'
            cur = a[-1]
            a.pop()
    elif a[0] > a[-1]:
        if cur < a[-1]:
            ans += 'R'
            cur = a[-1]
            a.pop()
        else:
            ans += 'L'
            cur = a[0]
            a.popleft()
    elif len(a) == 1:
        ans += 'R'
        cur = a[-1]
        a.pop()
    elif a[0] == a[-1]:
        cur1 = cur
        cur2 = cur
        b = a.copy()
        c = a.copy()
        count1 = 0
        count2 = 0
        while cur1 < b[0]:
            count1 += 1
            cur1 = b[0]
            b.popleft()
        while cur2 < c[-1]:
            count2 += 1
            cur2 = c[-1]
            c.pop()
        if count1 > count2:
            for i in range(count1):
                ans += 'L'
            break
        else:
            for i in range(count2):
                ans += 'R'
            break
    if len(a) == 0:
        break
print(len(ans))
print(ans)
