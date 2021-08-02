from collections import deque

s = input()
counter = 0
q = deque()
q.append("123123123123123")
for i in s:
    last = q.pop()
    if i != last:
        q.append(last)
        q.append(i)
    else:
        if last == i:
            counter += 1
print("Yes" if counter % 2 == 1 else "No")
