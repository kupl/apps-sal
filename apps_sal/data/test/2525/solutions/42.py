from _collections import deque
s = list(input())
s = deque(s)
q = int(input())
rev = False
for i in range(q):
    query = input()
    if len(query) == 1:
        rev = not rev
    else:
        x, f, c = query.split()
        if f == "1":
            if rev:
                s.append(c)
            else:
                s.appendleft(c)
        else:
            if rev:
                s.appendleft(c)
            else:
                s.append(c)
n = len(s)

if rev:
    ans = [s[n - 1 - i] for i in range(n)]
else:
    ans = [s[i] for i in range(n)]
print("".join(ans))
