from collections import deque
n = int(input())
s = input()
l_s = len(s)
cnt = 0
d = deque()
for i in s:
    if i == 'x':
        if len(d) > 1:
            o = d.pop()
            f = d.pop()
            if o == 'o' and f == 'f':
                cnt += 1
            else:
                d.append(f)
                d.append(o)
                d.append(i)
        else:
            d.append(i)
    else:
        d.append(i)
print(l_s - 3 * cnt)
