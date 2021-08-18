n = int(input())
events = []
for i in range(n):
    gender, a, b = input().split()
    a, b = int(a), int(b)
    events.append((a, -1, gender))
    events.append((b, 1, gender))
events.sort()
currM = 0
currF = 0
ans = 0
for ev in events:
    if ev[2] == "M":
        currM -= ev[1]
    else:
        currF -= ev[1]
    ans = max(ans, min(currM, currF) * 2)
print(ans)
