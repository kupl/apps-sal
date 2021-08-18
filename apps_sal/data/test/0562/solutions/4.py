n = int(input())

events = []
for i in range(n):
    l, r = list(map(int, input().split()))
    events.append((l, -1))
    events.append((r, 1))
events = sorted(events)
bal = 0
result = True
for item in events:
    bal += item[1] * (-1)
    if bal > 2:
        result = False
        print("NO")
        break
if(result):
    print("YES")
