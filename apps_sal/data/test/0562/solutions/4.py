n = int(input())

events = []
# -1 - start
for i in range(n):
    l, r = list(map(int, input().split()))
    events.append((l, -1))
    events.append((r, 1))
events = sorted(events)
bal = 0
result = True
for item in events:
    # print(item)
    bal += item[1] * (-1)
    # print(bal)
    if bal > 2:
        result = False
        print("NO")
        break
if(result):
    print("YES")
