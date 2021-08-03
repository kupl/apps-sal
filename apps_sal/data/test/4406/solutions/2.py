from collections import deque
a, b = map(int, input().split())
li = list(map(int, input().split()))
s = set()
l = deque([])
le = 0
for i in li:
    if i in s:
        pass
    elif le < b:
        le += 1
        s.add(i)
        l.appendleft(i)
    else:
        s.remove(l.pop())
        s.add(i)
        l.appendleft(i)
print(len(l))
print(*list(l))
