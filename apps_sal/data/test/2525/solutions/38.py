from collections import deque
s = input()
q = int(input())
inv = False
pr, su = deque(), deque()
for _ in range(q):
    query = input()
    if query[0] == '1':
        inv = not inv
    else:
        _, f, c = query.split()
        if inv:
            if f == '1':
                su.append(c)
            else:
                pr.append(c)
        else:
            if f == '1':
                pr.append(c)
            else:
                su.append(c)
ans = ''.join(pr)[::-1] + s + ''.join(su)
print(ans[::-1] if inv else ans)
